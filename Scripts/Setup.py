import argparse
import sys
import os
import subprocess


PREMAKE_LOCATION = "Libraries\Premake5\premake5.exe"
# "--file", "test.lua", 
PREMAKE_DEFAULT_ARGS = []
PREMAKE_SUPPORTED_BUILD_TARGETS = [
    "vs2022",
    "gmake2",
    "xcode4"
]



def GetArguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="A simple Python script that assists with setting up a sample C++ project")
    
    # Add command line arguments
    parser.add_argument(
        'build_target', help='Which build system Premake5 should target', choices=PREMAKE_SUPPORTED_BUILD_TARGETS
        )
    parser.add_argument('--git', action='store_true', help='Initialize a git repository for the project')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose mode')
    
    # Parse command line arguments
    return parser.parse_args()


def RunPremake(args: list[str]) -> bool:
    command = PREMAKE_LOCATION
    for arg in args:
        command = command + " " + str(arg)

    print(f"Running command: {command}")
    os.system(command)

    return True


if __name__ == "__main__":
    args = GetArguments()

    if args.git:
        os.system("git init")

    premake_arguments = PREMAKE_DEFAULT_ARGS + [args.build_target]
    RunPremake(premake_arguments)
