# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> function decorators
import time
import datetime

def decorator_templet(func):
    def wrapper(*args, **kwargs):
        print('started')
        to_return = func(*args, **kwargs)
        print('ended', end='\n\n')
        return to_return

    return wrapper

def before_after(func):
    def wrapper(*args):
        print('before')
        func(*args)
        print('after', end='\n\n')

    return wrapper

class Test:
    @before_after
    def decorated_method(self):
        print('run')

def timer_decorator(func):
    def wrapper():
        before = time.time()
        func()
        print('function took:', time.time() - before, 'seconds')

    return wrapper

def log_decorator(func):
    def wrapper(*args, **kwargs):
        with open('log.txt', 'a') as file:
            file.write('some info ')
        to_return = func(*args, **kwargs)
        return to_return

    return wrapper


# instance one
def normal(arg):
    print('normal ' * arg)

decorator_templet(normal)(2)
var = decorator_templet(normal)
var(4)


# instance two
@decorator_templet
def normal(arg, kwarg=None):
    print('normal ' * arg + kwarg)

normal(3, 'okay')


# instance three
@decorator_templet
def add(*args):
    result = 0
    for i in args:
        result += i
    print(result)
    return result

print(add(1, 3, 7, 15), end='\n\n')


# instance four: methods
test = Test()
test.decorated_method()


# instance five: timer
@timer_decorator
def run():
    time.sleep(2)

run()


# instance six: log
@log_decorator
def add(*args):
    result = 0
    for i in args:
        result += i
    print(result)
    return result

add(1, 3, 7, 15)
