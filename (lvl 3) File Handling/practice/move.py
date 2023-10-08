def filename(path):
    rpath = path[::-1]
    file_name = ''
    for i in rpath:
        if i == '\\':
            break
        else:
            file_name += i
    return file_name[::-1]


def filedir(path):
    length = len(path)-len(filename(path))
    dir_name = ''
    for i in range(0, length):
        dir_name += path[i]
    return dir_name


def rmgap(string):
    return string.replace(' ', '')


def display(src, dst):
    print('move: ' + src + '\nto: ' + filedir(dst), end='\n\n')


def main():
    import os

    item = 'trash\\risk of rain.txt'
    dst = 'risk of rain.txt'

    display(item, dst)

    try:
        if os.path.exists(dst):
            print('this directory: ' + filedir(dst))
            print('already contains a file called: ' + filename(item))
            inp = input('do you wont to overwrite it? (yes/no): ')

            if rmgap(inp.lower()) == 'yes':
                os.replace(item, dst)
                print(filename(dst) + ' has been overwritten')
                print(item + ' has been moved to:\n' + filedir(dst))
            else:
                pass
        else: 
            os.replace(item, dst)
            print(item + ' has been moved to:\n' + filedir(dst))

    except FileNotFoundError:
        print(item + ' (item not found)')

if __name__ == '__main__':
    main()
