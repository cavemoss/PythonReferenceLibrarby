# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> nested loops

rows = int(input('how many rows? '))
columns = int(input('how many columns? '))
symbol = input('what symbol? ')

for i in range(rows):
    for j in range(columns):
        print(symbol, end='')
    print()
