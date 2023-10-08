try:
    with open('log.txt') as file:
        print(file.read())
except Exception as error:
    print(error)

try:
    with open('log.tx') as file:
        print(file.read())
except FileNotFoundError:
    print('file not found')
