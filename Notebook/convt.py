import os
import nbformat
from nbformat.v4 import new_notebook, new_code_cell

def convert_py_to_ipynb(py_file_path, ipynb_file_path):
    with open(py_file_path, 'r') as py_file:
        code = py_file.read()
    nb = new_notebook(cells=[new_code_cell(code)])
    with open(ipynb_file_path, 'w') as ipynb_file:
        nbformat.write(nb, ipynb_file)

def convert_all_py_to_ipynb(root_dir):
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.py'):
                py_file_path = os.path.join(subdir, file)
                ipynb_file_path = os.path.splitext(py_file_path)[0] + '.ipynb'
                convert_py_to_ipynb(py_file_path, ipynb_file_path)
                print(f'Converted {py_file_path} to {ipynb_file_path}')

if __name__ == "__main__":
    root_directory = 'E:\\New folder\\Workshop\\Notebook'  # Replace with the path to your directory
    convert_all_py_to_ipynb(root_directory)
