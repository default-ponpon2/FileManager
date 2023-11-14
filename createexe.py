import os

try:
    os.remove('dist/FileManager.exe')
except FileNotFoundError as e:
    pass

os.system('pyinstaller --onefile FileManager.py')
