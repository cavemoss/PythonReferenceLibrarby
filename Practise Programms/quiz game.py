#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#quiz game

import messages as mess

questions ={'What do you get at the end of the Trile of the Conquerer?':'C',
            'How much essense is reqired to assend the Seer?':'B',
            'Which nail master gives you the Dash Slash?':'B',
            'Is Hornet Void?':'C'}

options =[['A. Charm Notch','B. wife','C. Pail Ore'],
          ['A. 1600','B. 2400','C. 2000'],
          ['A. Mato','B. Oro','C. Shio'],
          ['A. yas','B. iess','C. no.']]

def new_game():    
    guesses =[]
    currect_guesses =0
    question_number =1

    for key in questions:
        print('\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        print(key)
        for i in options[question_number-1]:
            print(i)
        guess =mess.inputF('your answer? ') 
        guesses.append(guess)
        currect_guesses += check_answare(questions.get(key),guess)
        question_number += 1

    desplay_score(currect_guesses, guesses)

def check_answare(answer, guess):
    if answer == guess:
        print('currect!')
        return 1
    else:
        print('wrong!')
        return 0
    
def desplay_score(currect_guesses, guesses):
    print('--------------------------------------------------')
    print('RESULTS')
    print('--------------------------------------------------')

    print('Answers', end=' ')
    for i in questions:
        print(questions.get(i), end=' ')
    print('')

    print('Guesses', end=' ')
    for i in guesses:
        print(i, end=' ')
    print('')

    score =int((currect_guesses/len(questions))*100)
    print('your score is ',str(score)+'%')

def play_again():
    response =mess.inputf('go again? ')
    if response == 'yes':
        return True
    else:
        return False

new_game()
while play_again():
    new_game()

print('ok byyyy!')