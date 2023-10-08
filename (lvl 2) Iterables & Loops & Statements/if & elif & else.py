# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> if statements

age = int(input('how old are you?'))

if age == 100:
    print('you are a century old')
elif age >= 18:
    print('you are an adult')
elif age < 0:
    print('you haven\'t been born yet')
else: 
    print('you are a child') 


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> logical operators

temp = int(input('what is the temperature outside?'))

if temp >= 0 and temp <= 30:
    print('the temperature is good outside\ngo outside')
elif temp < 0 or temp > 30:
    print('the temperature is bat today\nstay inside')

if not(temp >= 0 and temp <= 30):
    print('the temperature is bat today\nstay inside')
elif not(temp < 0 or temp > 30):
    print('the temperature is good outside\ngo outside')
