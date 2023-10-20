# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> walrus operator

happy = False
print(happy)
print(happy := True)

foods = list()
while True:
    food = input('what do you like to e-eat? ')
    if food == 'quit':
        break
    foods.append(food)

for i in foods:
    print(i, end=', ')

foods2 = list()
while food := input('what would you like to eat? ') != 'quit':
    foods2.append(food)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> min max value

number = 101
max_value = 100
min(number, max_value)

number = 999
min_value = 1000
max(number, min_value)
