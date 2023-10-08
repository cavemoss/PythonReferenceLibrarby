# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> string.format()

who = 'cow'
what = 'moon'

print('the ' + who + ' jumped over the ' + what)

print(f'the {who} jumped over the {what}')
print('the {} jumped over the {}'.format(who, what))
print('the {2} jumped over the {0}'.format(who, what, 'cat'))
print('the {who} jumped over the {what}'.format(who='moon', what='cow'))

text = 'the {} jumped over the {}'
print(text.format(who, what))

name = 'Ralsey'
print('hello, my name is {}'.format(name))
print('hello, my name is {:10}. its nice to meet you'.format(name))
print('hello, my name is {:>10}{:^20}. its nice to meet you'.format(name, 'wath?'))

num = 3.14259
print('the number pi is {:.2f}'.format(num))

num2 = 1000000
print('look an the number: {:,}'.format(num2))

num3 = 192
print('look an the number: {:b}'.format(num3))
print('look an the number: {:o}'.format(num3))
print('look an the number: {:x}'.format(num3))
print('look an the number: {:e}'.format(num3))
