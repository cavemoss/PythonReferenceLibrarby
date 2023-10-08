print('Create a new .txt file at: trash\\')
name = input('Name of the .txt file: ')
text = input('Input the text: ')
numb = input('Times: ')

with open('trash\\' + name + '.txt', 'w') as file:
    file.write(str(text)*int(numb))
