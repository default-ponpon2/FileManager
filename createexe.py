import os

#try:
#    print('Removing old FileManager.exe')
#    os.remove('dist/FileManager.exe')
#except FileNotFoundError as e:
#    pass

os.system('pyinstaller --onefile FileManager.py')

# kek
