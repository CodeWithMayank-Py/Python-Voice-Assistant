import os
import subprocess as sp

# Add Paths of the software you wanna add.
# Notepad, Calculator, Google, Camera

paths = {
    "Notepad":"C:\\Windows\\notepad.exe",
    "Calculator":"C:\\Windows\\System32\\calc.exe",
    "Google":"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
}

# open the camera

def open_camera():
    sp.run('start microsoft.windows camera:', shell=True)

# Open the Desktop application paths we added

# Open Notepad
def open_notepad():
    os.startfile(paths["Notepad"])

# Open Calculator
def open_calc():
    os.startfile(paths["Calculator"])

# Open Google
def open_google():
    os.startfile(paths["Google"])

# Open Command prompt
def open_cmd():
    os.system("start cmd")