# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> string methods

name = 'mosssDy'

values = [
    len(name),                  # len (count how many characters)
    name.find('D'),             # find (find a character within a string)
    name.capitalize(),          # capitalize (capitalize first character)
    name.upper(),               # upper (make all characters uppercase)
    name.lower(),               # lower (make all characters lowercase)
    name.isdigit(),             # isdigit (make sure if the characters are digits)
    name.isalpha(),             # isalpha (make sure if the characters are alphabet)
    name.count('o'),            # count (count how many there is of sayed character)
    name.replace('0', 'a')      # replace (replace all arg_one with arg_two)
]

for i in values:
    print(i)
