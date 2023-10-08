#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#rock paper sceissors

import random 
import messages as mess
print('play rps with me :3')
choices =['rock','paper','sceissors']

while True:
    comp =random.choice(choices)
    you =mess.inputf('go for it! ')     
      
    while you not in choices:
        print('ahhh...')

    if comp == you:
        print('Tie!')

    elif you == 'paper':
        if comp == 'rock':
            print('you win bruh(')
        elif comp == 'sceissors':
            print('I allways win')

    elif you == 'rock':
        if comp == 'sceissors':
            print('you win bruh(')
        elif comp == 'paper':
            print('I allways win')

    elif you == 'sceissors':
        if comp == 'paper':
            print('you win bruh(')
        elif comp == 'rock':
            print('I allways win')

    print('me: '+comp)
    print('you: '+you)

    again =mess.inputf('wonna play again?')
    if not again =='yes':
        break
print('ok byee')