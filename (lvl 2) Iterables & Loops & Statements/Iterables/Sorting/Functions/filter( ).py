# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> filter()

the_bois = [('boi1', 19),
            ('boi2', 18),
            ('boi3', 17),
            ('boi4', 16),
            ('boi5', 20),
            ('boi6', 21)]

drinking_bois = list(filter(lambda data: data[1] >= 18, the_bois))

for i in drinking_bois:
    print(i)
