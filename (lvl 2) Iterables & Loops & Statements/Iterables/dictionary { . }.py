# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> dictionary {key:value}

empty_dictionary = dict()

capitals = {'USA': 'Washington DC',
            'England': 'London',
            'France': 'Paris'}

for key, value in capitals.items():
    print(key, value)

print(capitals['England'])
print(capitals.get('Germany'))              # get(key) (returns value of a key, safer way)
print(capitals.keys())                      # keys (list all keys)
print(capitals.values())                    # values (list all values)
print(capitals.items())                     # items (list both keys and values)

capitals.update({'Germany': 'Berlin'})      # update (update or correct a dictionary)
print(capitals.get('Germany'))

capitals.update({'USA': 'Moscow'})
for country, capital in capitals.items():
    print(country, capital)

capitals.pop('France')                      # pop  (remove an entry)
capitals.clear()                            # clear  (clear the dictionary)
