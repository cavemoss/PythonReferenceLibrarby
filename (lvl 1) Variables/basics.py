# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> print('string')

print('write strings like this\nif it requires more lines', end='\n\n')

print('backwards slash is the escape symbol, so you can print <don\'t>', end='\n\n')
print("you can also use double quotes for that purpose <don't>", end='\n\n')

print('this is \t how you \t do tabs', end='\n\n')

print('''write strings like this 
if it requires more lines''', end='\n\n')


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> assign and print()

a = 'string'
b = 42
c = 4.2
d = True
print(a, b, c, d, sep=' | ')

a, b, c, d = 'another string', 47, 5.3, False
print(a, b, c, d, sep=' | ', end='\n\n')

a, b, c, d = 'the other string', \
             911, \
             42.42, \
             True
print(a, b, c, d, sep=' | ', end='\n\n')


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> typecasting

print(type(a),
      type(b),
      type(c),
      type(d),
      end='\n\n')

print(a + ' ' + str(b) + ' ' + str(c) + ' ' + str(d))
print(bool(a), bool(b), bool(c), bool(d))
print(b + int(c))
print(float(b))
print(c + float(b), end='\n\n')


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> input()

desire = input('what do you want? ')
print('you ain\'t getting ' + desire)

number = float(input('give me a number '))
other_number = float(input('give me some other number '))

print('i divided them for u <3\n' + str(number/other_number), end='\n\n')


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> del

del a, b, c, d
print(a, b, c, d)
