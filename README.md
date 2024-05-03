# Debugging Python scripts in Blender with VSCode

This repo contains an example project to write and debug python scripts written for 
Blender in VSCode on a Windows machine. The goal was to be able to
- write python code in VSCode with all the editor goodies it has, like proper code 
coloring, code completion and so on
- attach a a debugger and debug python, being able to inspect variables and objects
- import code from additional python files
- use your own virtual environment and pip install and use additional modules
- do all of the above without the need of unofficial extensions or dependencies

## Motivation
1. Blenders built-in python editor has not a whole lot of features for coding, most
prominently there is no code completion
2. Blender has no built-in debugger for python scripts
3. Most tutorials to debug python scripts in blender either refer to 
    - [AlansCodeLog's blender-debugger-for-vscode](https://github.com/alanscodelog/blender-debugger-for-vscode) repo which seems to be meant for building and debugging blender addons, 
    but not python scripts to modify a blender scene. 
    - [JacquesLuke's blender_vscode](https://github.com/JacquesLucke/blender_vscode) 
    extension for VSCode which according to the repo description is not actively 
    developed anymore (although it probably still works fine). 


## Step-by-step instruction

1. Download and install blender from http://blender.org
2. (Optional) add blender to your PATH environment variable. Since blender is started 
from the console in this setup, this will make life easier later. 
    - In Windows got Control Panel
    - Selet System
    - Select Advanced System Settings
    - Go to the Advanced tab
    - Press the "Environment Variables" button at the bottom
    - Under "System variables" find the `Path` variable, select it and press "Edit..."
    - Add the path to your blender installation folder (the directory containing blender.exe)
With this you should be able to open blender via the console from any location
3. Next step is to create a virtual environment. The Major and Minor version number **MUST** match
the version of the original python installation that came with blender. In case of Blender 4.1 this
was python version 3.11.7. Otherwise this can be easily checked by opening a terminal 
and using the commmand `<blender-installation-folder>/4.1/python/bin/python.exe --version`
With the correct system installation open a console or Powershell window 
and go to `<blender-installation-folder>/4.1/`. 
The command to create a virtual environment in the right folder- assuming python launcher on windows is installed - 
is `py -3.11 -m venv python`. This should put the venv into the already existing python folder.
4. Find the python subfolder and delete the `bin` folder within. Our new python.exe is within the `Scripts` folder. 
5. Since Blender expects a python exe in the bin folder, we need to run the following command within the 
python folder: `mklink /d "<blender-installation-folder>/4.1/python/bin" "<blender-installation-folder>/4.1/Scripts"`
This will create a link between the created venv and the location where blender expects python. 
6. Clone this repo and open it in VSCODE
7. Select blenders python environment as python interpreter:
    - Press Ctrl+Shift+P and write `Python: Select Interpreter`
    - Select `Enter interpreter path...`
    - Find and select the correct python.exe under `<blender-installation-folder>/4.1/python/Scripts/python.exe`
8. Install needed python dependencies: 
    - The project is setup to work as pip package. Any needed dependencies are listed in `setup.cfg`
    - Go to Terminal -> new Terminal and type `pip install -e .` to install the project as pip package. 
     The `e` flag means `editable` which means changes to the code will be reflected in the installed package.
     The advantage of installing the code base as pip package is to avoid the hassle with import paths. 
     We can simply import from `blenderhelloworld`. 
    - Additionally we need to install debugpy via `pip install debugpy` this is only necessary once for a 
    new blender installation. 
9. Open Blender from a VSCode Terminal:
    - Go to Terminal -> new Terminal
    - If you followed step 2 blender can be started by simply typing blender into the terminal
    and pressing Enter. Otherwise you have to enter the full path or navigate to the Blender installation folder
10. (Optional) Code checking and linting:
    - The projects settings.json already includes settings include blenders internal packages pylance's code checking, only the path in `python.analysis.extraPaths` needs to be adapted. 
    - Additionally options are set to use code checkers/linters. I always use and highly recommend [black](https://black.readthedocs.io/en/stable/) and [ruff](https://docs.astral.sh/ruff/). 
    These two can simply be installed via `pip install black ruff`. For black I recommend default settings. Ruff options can be changed in the `ruff.toml` file. 
11. Write and debug code! :)
    - The project is only a starting point, it includes a simple main.py and one additional python file
    to test local imports imports
    - In order to debug, copy the contents of `launch.py` into blenders scripting editor and 
    adapt the `script_path` variable to point to your actual `main.py`
    - Press `Run Script` in Blender. It will start a debug server and listen. This means Blender will freeze
    until a debugger is attached. To attach the debugger, simply go to `Run and Debug` menu in VSCode and 
    start `Blender Attach`. The launch.json settings for for it are already set and should work out-of-the-box.


## Questions or Problems?

In case of questions or problems please just open a new issue on the repo. 