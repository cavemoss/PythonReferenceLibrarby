# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> exception handling

try:
    nominator = int(input('nominator: '))
    denominator = int(input('denominator: '))
    result = nominator/denominator
except ZeroDivisionError as error:
    print(error, end='. ')
except ValueError as error:
    print(error, end='. ')
except Exception as error:
    print(error, end='. ')
    print('something went wrong')
else:
    print(result)
finally:
    print('this will always execute')
