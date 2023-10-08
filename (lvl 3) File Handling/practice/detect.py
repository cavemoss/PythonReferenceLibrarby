import os
way = "C:\\Users\\alexs\\Desktop\\blueprints"

if os.path.exists(way):                        
    print('this location exists')
    if os.path.isfile(way):
        print('its a file')
    elif os.path.isdir:
        print('its a directory')
else:
    print('this location doesnt exist')
