# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> string methods

name = 'mosssDy'

values = [
    len(name),                  # len (count how many characters) -> int
    name.find('D'),             # find (find a character within a string) -> int
    name.capitalize(),          # capitalize (capitalize first character) -> str
    name.upper(),               # upper (make all characters uppercase) -> str
    name.lower(),               # lower (make all characters lowercase) -> str
    name.isdigit(),             # isdigit (make sure if the characters are digits) -> bool
    name.isalpha(),             # isalpha (make sure if the characters are alphabet) -> bool
    name.count('s'),            # count (count how many there is of sayed character) -> int
    name.replace('o', 'a'),     # replace (replace all arg_one with arg_two) -> str
    name.split('sss')           # split (split the string up on a certain character) -> list[str]
]

for i in values:
    print(i)
