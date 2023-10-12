# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> map()

store_dollar = [('shirt', 20.00),
                ('hoodie', 40.00),
                ('water bottle', 16.00)]

store_euro = list(map(lambda data: (data[0], data[1]*0.82), store_dollar))

for i in store_euro:
    print(i)
