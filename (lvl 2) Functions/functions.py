# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> def function

def function(argument, key_word=None):
    """
    Epic Style comments
    exclusive for functions
    :param argument:
    :param key_word:
    :return:
    """
    pass
function('', key_word='')


def hello(who):
    print('greetings, ' + who)
    print('it is nice to meet you')
hello('my friend')


def sey_times(what, times):
    print((what+' ')*times)
sey_times('leave', 10)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> local vs global scope

name = 'bro'


def display_name():
    name = 'code'
    print(name)

print(name, end='')
display_name()


def display_name_cool():
    global name
    other_name = 'code'
    print(name + ' ' + other_name)

display_name_cool()


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> return statements

def multiply(one, two):
    res = one*two
    return res
print(multiply(2, 2))


def power(one, two):
    return one**two
print(power(23, 2))


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> assigning function to a variable

def hello():
    print('hello')
print(hello)

hi = hello
print(hi)

hello()
hi()

say = print
say('whatever')


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> keyword arguments \ parameters

def hello(first_name, middle_name, last_name):
    return 'hi '+first_name+' '+middle_name+' '+last_name

print(hello('bro', 'mate', 'fella'))
print(hello(last_name='bro', first_name='mate', middle_name='fella'))


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> nested function calls

num = input('enter a number that is cool: ')
num = float(num)
num = abs(num)
num = round(num)
print(num)

print(round(abs(float(input('enter some another cool number now! ')))))
