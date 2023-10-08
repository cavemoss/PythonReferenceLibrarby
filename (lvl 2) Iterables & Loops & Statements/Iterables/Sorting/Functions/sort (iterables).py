# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> sort()

these = ['A', 'F', 'B', 'D', 'C']

these.sort()
for i in these:
    print(i, end='')
print()

these.sort(reverse=True)
for i in these:
    print(i, end='')
print()


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> sorted()

those = ('A', 'F', 'B', 'D', 'C')

those_sorted = sorted(those)
for i in those_sorted:
    print(i, end='')
print()

those_sorted = sorted(those, reverse=True)
for i in those_sorted:
    print(i, end='')
print()


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> sort tuples with sort()

the_bois = [('Squidward', 'F', 60),
            ('Sandty', 'A', 33),
            ('Patrick', 'D', 36),
            ('Spongebob', 'B', 20),
            ('Mr.Krabs', 'C', 78)]

the_bois.sort()
for i in the_bois:
    print(i)
print('\n')


the_bois.sort(key=lambda grades: grades[1])
for i in the_bois:
    print(i)
print('\n')

the_bois.sort(key=lambda grades: grades[1], reverse=True)
for i in the_bois:
    print(i)
print('\n')


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> sort tuples with sorted()

the_lads = (('Squidward', 'F', 60),
            ('Sandty', 'A', 33),
            ('Patrick', 'D', 36),
            ('Spongebob', 'B', 20),
            ('Mr.Krabs', 'C', 78))

the_lads_sorted = sorted(the_lads, key=lambda age: age[2])
for i in the_lads_sorted:
    print(i)
