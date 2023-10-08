print('----------------------------')
print('APPEND TEXT TO THIS .PY FILE')
print('----------------------------')

text = input('Input the text: ')
numb = input('Times: ')

with open('append.py', 'a') as file:
    file.write('\n\n#')
    file.write(str(text)*int(numb))
