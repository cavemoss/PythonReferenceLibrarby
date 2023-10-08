# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> lambda function

def double(num):
    return num + num


print(double(5))

dob = lambda x: x * 2
mult = lambda x, y: x * y
add = lambda x, y, z: x + y + z
full_name = lambda first, last: first + '' + last
age_check = lambda age: True if age >= 18 else False

print(dob(5))
print(mult(5, 20))
print(add(5, 20, 200))
print(full_name('bro', 'code'))
print(age_check(19))
