# detect file
import os

way = "path\\name"
if os.path.exists(way):
    print('found', end=' ')
    if os.path.isfile(way):
        print('file')
    elif os.path.isdir:
        print('directory')
else:
    print('not found')


# read file
try:
    with open('path\\name') as file:
        print(file.read())
except Exception as error:
    print(error)


# create a file
text = ''
with open('path\\name','w') as file:
    file.write(text)
file.close()


# append a file
with open('path\\name','a') as file:
    file.write(text)
file.close()


# copy file
import shutil   

shutil.copyfile('src', 'dst')
shutil.copy('src', 'dst')
shutil.copy2('src', 'dst')


# move file
import os

item = 'path\\name'
dst = 'path\\name'

try:
    os.replace(item,dst)
    print(item + ' has been moved to: ' + dst)
except Exception as error:
    print(error)


# delete a file
import os

try:
    os.remove('path\\name')
except Exception as error:
    print(error)


# delete an empty folder
import os

try:
    os.rmdir('path')
except Exception as error:
    print(error)


# delete a tree folder
import shutil

try:
    shutil.rmtree('path')
except Exception as error:
    print(error)
