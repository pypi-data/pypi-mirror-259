
""""
PyGM (Python Git module)
Git based module/package manager for Python.

### Import (function)
Pulls the module from the Git repository and returns the module.
If the repository contains multiple Python files, the result module will contain a field for each file.
If the repository contains only one Python file, the result module will be the file.

### Use (function)
Pulls the module from the Git repository and returns a list of the Python files in the directory.
"""
import os
import ezstools.module_tools as mt
from types import ModuleType

RepoUrl = str


def complete_repo_url(repo: RepoUrl) -> RepoUrl:
    if repo.startswith('/'):
        repo = repo[1:]

    repo = f'https://github.com/{repo}'
    return repo  

def path_to_module_name(path: str) -> str:
    if path.startswith('/'):
        path = path[1:]
    if path.endswith('/'):
        path = path[:-1]
    if path.startswith('./'):
        path = path[2:]

    return path.replace('/', '.')


def filename_to_module_name(filename: str) -> str:
    if not filename.endswith('.py'):
        raise Exception('The file is not a Python file can\'t be imported as module')

    return filename.replace('.py', '')

def Use(repo: RepoUrl, save_path: str) -> list[str]:
    """
    Clone or pull a Git repository. 
    repo: The URL of the Git repository. or {username}/{repo}   
    save_path: The path to save the repository to.

    Creates a __init__.py file in the directory if it does not exist.
    Returns a list of the python files in the directory.
    """
    # Check if the repo is a full URL or just the username and repo name
    if 'github.com' not in repo:
        repo = complete_repo_url(repo)

    # Check if path exists
    if not os.path.exists(save_path):
        clone_result = os.system(f'git clone {repo} {save_path} --depth 1')
    else:
        # check if directory contains a .git folder
        if not os.path.exists(f'{save_path}/.git'):
            raise Exception('The directory already exists and does not contain a .git folder. Can\'t check versions')
        
        # If it does, pull the latest version if not already up to date
        pull_result = os.system(f'git -C {save_path} pull -q')

        if pull_result != 0:
            raise Exception('Failed to pull the latest version of the repository.')
        
        clone_result = 0

    if clone_result != 0:
        raise Exception('Failed to clone the repository. Perhaps the directory already exists.')
    

    # Create __init__.py inside the directory if it does not exist
    if not os.path.exists(f'{save_path}/__init__.py'):
        with open(f'{save_path}/__init__.py', 'w') as f:
            f.write('')

    files = [file for file in os.listdir(save_path) if file.endswith('.py') and file != '__init__.py']


def Import(repo: RepoUrl, save_path: str) ->  ModuleType:
    """
    Import a module from a Git repository.
    repo: The URL of the Git repository. or {username}/{repo} 
    save_path: The path to save the module to.

    Returns a module.
    """
    # If multiple files -> Each file is a module, result module will contains a field per file
    # If one file -> The file is the module and the result module will be the file

    files = Use(repo, save_path)  

    mod_loc = path_to_module_name(save_path)

    if len(files) == 0:
        raise Exception('The repository does not contain any Python files')

    if len(files) == 1:
        # Execute the file and return the result
        return __import__(f'{mod_loc}.{filename_to_module_name(files[0])}', fromlist=[mod_loc])

    else:
        # Create a module with a field for each file
        return mt.create_module(
            mod_loc,
            {file: __import__(f'{mod_loc}.{filename_to_module_name(file)}') for file in files}
        )

