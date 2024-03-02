import sys
import os

def Module(node) -> bool:
    node_is_a_python_file = node.name.endswith('.py')
    node_is_init = node.name.endswith('__init__.py')
    node_is_pycache = node.name.endswith('__pycache__')
    node_ends_with_info = node.name.endswith('-info')
    node_is_a_directory = os.path.isdir(node.name)
    return ((node_is_a_python_file and (not node_is_init)) or node_is_a_directory) and (not node_is_pycache and not node_ends_with_info)