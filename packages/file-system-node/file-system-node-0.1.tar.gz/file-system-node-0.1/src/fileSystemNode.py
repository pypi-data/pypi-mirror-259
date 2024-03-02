# graphFolderStructureModel.py

import os
import re
from anytree import Node, findall, PreOrderIter
from typing import List
from typing import Callable

import sys
import os

def import_the_folder_n_steps_above(n: int) -> None:
    current_folder = os.path.abspath(os.path.dirname(__file__))
    steps = [".."] * n
    target_folder = os.path.abspath(os.path.join(current_folder, *steps))
    sys.path.insert(0, target_folder)
import_the_folder_n_steps_above(n=1)
import_the_folder_n_steps_above(n=2)

from src.internalFunctions.predicates import Module

def is_valid_path(path: str) -> bool:
    return os.path.exists(path)

class PathString(str):
    def __new__(cls, path):
        if not is_valid_path(path):
            raise ValueError("The path is not valid.")
        return super().__new__(cls, path)

    def getContents(self) -> List[str]:
        if os.path.isfile(self) and not self.endswith(".pyc"):
            with open(self, 'r') as file:
                contents = file.readlines()
                return contents
        return []

class FileSystemNode(Node):
    packagesHoldingExternalModules = ["venv/lib/python3.8/site-packages"]

    def __init__(self, path: PathString, parent=None, children=None, **kwargs):
        path = PathString(path)#String could be passed, so explicit cast is required, even though type enforcing have been done in the parameter list.
        super().__init__(path, parent, children)
        self.__dict__.update(kwargs)
        self.contents = path.getContents()

    def print_children(self):
        for child in self.children:
            print(child.path)
            child.print_children()

    def find_files_matching_pattern(self, pattern, onlyNames=False) -> List:
        accessiblePathNodes = findall(self, lambda node: re.match(pattern, node.name))
        return [os.path.basename(pathNode.name) for pathNode in accessiblePathNodes] if onlyNames else accessiblePathNodes
    
    def getTests(self, onlyNames=False):
        return self.find_files_matching_pattern(r'.*test.*\.py$', onlyNames)

    def getImportLines(self):
        return [line for line in self.contents if line.startswith(('import ', 'from '))]
    
    def getImportedSoftwareElements(self):
        importLines = self.getImportLines()
        importedObjects = []
        for line in importLines:
            if line.startswith('import '):
                # For "import module" or "import module as alias", the object is the module
                importedObjects.append(line.split()[1].split(' as ')[0])
            elif line.startswith('from '):
                # For "from module import object" or "from module import object as alias", the object is the object
                importedObjects.append(line.split()[3].split(' as ')[0])
        return importedObjects
    
    def getSoftwareModuleNamesInvolvedInImports(self):
        importLines = self.getImportLines()
        return [line.split()[1].split(".")[-1] for line in importLines]

    @staticmethod
    def get_directory_structure(path: PathString) -> 'FileSystemNode':
        node = FileSystemNode(path)
        badExtensions = [".pyc", ".so", ".exe", ".gz", ".a", ".o"]
        if os.path.isdir(path):
            node.children = [FileSystemNode.get_directory_structure(os.path.join(path, child_path)) for child_path in os.listdir(path) if not any(child_path.endswith(extension) for extension in badExtensions)]
        return node

    #TODO: Implement this correctly!
    @staticmethod
    def get_names_of_external_modules_used():
        external_modules = []
        for path in FileSystemNode.packagesHoldingExternalModules:
            root_node = FileSystemNode.get_directory_structure(PathString(path))
            for node in PreOrderIter(root_node):
                if Module(node):
                    external_modules.append(os.path.basename(node.name))
        return external_modules

    def getModulesUsedDuringImportingOfDescendantsAndTheCurrentNode(self):
        node = FileSystemNode.get_directory_structure(self.name)
        modulesUsedDuringImporting = []
        modulesUsedDuringImporting.extend(node.getModulesUsedDuringImportingOfDescendantsAndTheCurrentNode())
        for descendant in node.descendants:
            modulesUsedDuringImporting.extend(descendant.getSoftwareModuleNamesFromWhichImportingWasDone())
        return modulesUsedDuringImporting
    
    def checkPropertyOnTheElementsOfDirectoryStructure(self, property:Callable[['FileSystemNode'], bool]):
        root_node = FileSystemNode.get_directory_structure(self.name)
        for node in PreOrderIter(root_node):
            if not property(node):
                return False
        return True