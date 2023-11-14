import os

try:
    print('Removing old FileManager.exe')
    os.remove('dist/FileManager.exe')
except FileNotFoundError as e:
    pass
print('Old File was deleted nahuy')

os.system('pyinstaller --distpath build/test --onefile FileManager.py')
