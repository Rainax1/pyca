# Native
import os.path
import subprocess
import sys

#PyInstaller
pyInstallerInstalled = True

try:
    import PyInstaller.__main__ as PyInstaller
except ImportError:
    pyInstallerInstalled = False

# Async @ True
# app @ Async
# All @ Async

# Async defunc app(string :: Str) :: Str {
#        "{string}" fcwriteln
#    } 


#Custom
from err import Error
from parser import Parser

class Interpreter:
    def __init__(self) -> None:
        if os.name == "nt":
            subprocess.call(["python", "output.py"])
        else:
            subprocess.call(["python3", "output.py"])
