# Lib Potato

Sample project for generating C++ project structures. See the template repository, [Potato C++](https://github.com/Anthony-J-G/potato-cpp) version 1.0.0, hosted on Github.


## Development

If you wish to compile the repository from the source, see the [building instructions](Docs/BUILDING.md) in `Docs/BUILDING.md`.


Potato C++ requires [Premake5](https://premake.github.io) for generation of project files.

Run `python Scripts/Setup.py` to generate build files for the project, passing a command line arguement of `vs2022` or `gmake` to generate files for Visual Studio 2022 and Makefile, respectively. Additionally, passing `--git` to `Scripts/Setup.py` will automatically initialize a .git repository for the folder.

All project files get removed from running `python Scripts/Clean.py`.
