"""
    Simple Python script for assisting in cleaning build files from a C++ project.

    Note from the Author: This script is designed to help bulk remove garbage files from a project and should be used with care.

"""


import argparse
import sys
import os
import subprocess
import shutil



def PATHIFY(name):
    return f"\\{name}"


PREMAKE_LOCATION = "Libraries\Premake5\premake5.exe"
PREMAKE_ARGS = ["vs2022"]

EXTERNAL_DIR_NAME = f'.\\Libraries'

DIRTY_DIRECTORIES = [
    ".\\Binaries",
    ".\\Intermediate",
]
DIRTY_FILE_TYPES = {
    ".vcxproj", ".sln", ".user"
}


def GetArguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="A simple Python script that cleans a codebase of any non-")
    
    # Add command line arguments
    parser.add_argument('--verbose', action='store_true', help='Enable verbose mode')
    
    # Parse command line arguments
    return parser.parse_args()


def ShouldIgnoreDir(directory_name: str) -> bool:
    isGit = '\\.git' in directory_name or '\\.git\\' in directory_name

    isExternal = directory_name[:len(EXTERNAL_DIR_NAME)] == EXTERNAL_DIR_NAME

    return isGit or isExternal


def IsDirtyFile(filepath: str) -> bool:
    _, file_extension = os.path.splitext(filepath)
    file = os.path.basename(_)
    
    isDirtyExtension = file_extension in DIRTY_FILE_TYPES
    isMakefile = file == "Makefile"

    return isDirtyExtension or isMakefile


def FindDirtyFiles(root_directory: str) -> list[str]:
    # List to store found files
    dirty_files = []

    for root, dirs, files in os.walk(root_directory):
        if ShouldIgnoreDir(root):
            continue        

        for file in files:
            path = os.path.join(root, file)

            if IsDirtyFile(path):
                dirty_files.append(path)

    return dirty_files


def CullDirectories() -> None:
    for dir in DIRTY_DIRECTORIES:
        try:
            shutil.rmtree(dir)
        except FileNotFoundError:
            pass


def CullFiles(files: list[str]) -> None:
    for file in files:
        try:
            os.remove(file)
        except FileNotFoundError:
            continue


def PrintFiles(files: list[str]) -> None:
    # Print the result
    for file_path in files:
        print(file_path)


def VerifyCull(num_files) -> bool:
    size = 0
    for dir in DIRTY_DIRECTORIES:
        try:
            print(dir, shutil.disk_usage(dir))

        except FileNotFoundError:
            pass

    print(f"Removing {len(DIRTY_DIRECTORIES)} directories and {num_files} files")
    response = ""
    while response.lower() != "n":
        response = input("Proceed? (Y/n)")

        if response.lower() == "y":
            return True

    return False



if __name__ == "__main__":
    args = GetArguments()

    # Example usage:
    root_directory = '.'
    result = FindDirtyFiles(root_directory)

    if VerifyCull(len(result)):
        CullDirectories()
        CullFiles(result)
