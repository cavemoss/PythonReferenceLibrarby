import os

try:
    path = 'trash\\risk of rain.txt'
    os.remove(path)
except FileNotFoundError:
    print('FileNotFoundError bruh')

try:
    os.remove('a folder')
except Exception as error:
    print(error)


try:
    os.rmdir('an empty folder')
except Exception as error:
    print(error)


import shutil

try:
    shutil.rmtree('a folder')
except Exception as error:
    print(error)
