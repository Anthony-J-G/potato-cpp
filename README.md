# Potato C++

Sample project for generating C++ project structures. This project was generated with [Potato C++](https://github.com/Anthony-J-G/potato-cpp) version 1.0.0.


## Project File Generation

Potato C++ requires [Premake5](https://premake.github.io) for generation of project files.

Run `python Scripts/Setup.py` to generate build files for the project, passing a command line arguement of `vs2022` or `gmake` to generate files for Visual Studio 2022 and Makefile, respectively. Additionally, passing `--git` to `Scripts/Setup.py` will automatically initialize a .git repository for the folder.

All project files get removed from running `python Scripts/Clean.py`.