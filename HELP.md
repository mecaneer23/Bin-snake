# Help
This document provides help with simple running - especially if you have never run a program before.

## Running python (.py)
### Windows
On Windows, running python is quite simple, just make sure you have installed Python:

#### Installing Python
1. Visit [python.org](https://www.python.org/downloads/)
2. Download the latest version of python for Windows
3. Open the download box (likely in the lower left corner of your screen) and run the installer
4. IMPORTANT: when prompted to add Python to PATH, make sure to check the box, otherwise you won't be able to run python easily

#### Running Python
1. Open a command prompt (cmd) - the easiest way is to press the windows key on your keyboard (between left ALT and CTRL) and type "cmd"
2. Go to the directory of the python file you want to run - if you open File Explorer there is a path to each file, which you can type in manually or copy. It should look something like: `C:\Users\<username>\Desktop\Code\`, in cmd, type: `cd`, followed by the path.
3. Type: 
```
python filename.py
```
4. After pressing `ENTER`, you should see the result of your code.

### Linux (and MacOS)
On Linux, python3 should be preinstalled. There are two ways to run a python file:

#### Running in current directory
To run a file in the current directory, ensure the first line of the file has the location of the executable you want to use, for example:
```py
#!/bin/python3
```
Then, you can run your python file as:
```
./filename.py
```

#### Running in python3
For this to work, the first line doesn't have to be anything specific, but the run command is slightly longer:
```
python3 filename.py
```
