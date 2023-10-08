# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> if __name__ == '__main__'
import module_two


def function():
    print('something important')

if __name__ == '__main__':
    print('running directly')
else:
    print('running another indirectly')

if __name__ == '__main__':
    print(__name__)
    print(module_two.__name__)
    function()
