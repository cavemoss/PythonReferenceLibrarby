# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> exception handling

try:
    nom = int(input('nominator: '))
    denom = int(input('denominator: '))
    res = nom/denom
except ZeroDivisionError as error:
    print(error, end='. ')
    print('you\'re dumb?')
except ValueError as error:
    print(error, end='. ')
    print('you testin\' me?')
except Exception as error:
    print(error, end='. ')
    print('something went wrong')
else:
    print(res)
finally:
    print('this will always execute')
