import shutil

with open('read this.txt', 'w') as file:
    file.write('')

shutil.copyfile('read this.txt', 'trash\\copy read this.txt')
shutil.copy('read this.txt', 'trash\\copy read this2.txt')
shutil.copy2('read this.txt', 'trash\\copy read this3.txt')
