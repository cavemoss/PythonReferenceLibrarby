# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> *arg = list()

def add(num1, num2):
    return num1 + num2

print(add(1, 123))


def add_2(*arg):
    value = 0
    for i in arg:
        value += i
    return value

print(add_2(1, 123, 243, 2342))


def add_3(*arg):
    value = 0
    stuff = list(arg)
    stuff[0] = 0
    for i in stuff:
        value += i
    return value

print(add_3(3, 2))


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> **kwarg = dict()


def hello_cool(**kwargs):
    try:
        print('hi ' + kwargs['first'] + ' ' + kwargs['last'])
    except KeyError:
        pass
    print('greetings!', end=' ')
    for key, value in kwargs.items():
        print(value, end=' ')

hello_cool(title='Ms.',
           first='Bro',
           middle='Mate',
           last='Code')
