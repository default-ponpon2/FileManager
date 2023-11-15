import os

#try:
#    print('Removing old FileManager.exe')
#    os.remove('dist/FileManager.exe')
#except FileNotFoundError as e:
#    pass

os.system('pyinstaller --distpath --onefile FileManager.py')

# kek
