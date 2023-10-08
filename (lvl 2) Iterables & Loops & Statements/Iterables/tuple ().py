# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> tuple ()

empty_tuple = tuple()

specimen = ('Mate', 'Mate', 21, 'boi', 'boi')

print(specimen.count('Mate'))
print(specimen.index('boi'))

for i in specimen:
    print(i, end=' ')
print('')

if 'Mate' in specimen:
    print('Mate is here')
