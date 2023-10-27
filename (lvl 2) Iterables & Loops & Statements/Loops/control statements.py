# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> loop control statements

while True:
    name = input('give me your name? ')
    if not name == '':
        break

for i in range(1, 20 + 1):
    if i == 13:
        pass
    else:
        print(i)

text_string = '192.169.1.47'
print(text_string.replace('.', ''))
for i in text_string:
    if i == '.':
        continue
    print(i, end='')
