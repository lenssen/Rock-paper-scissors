
import random
n = 1
user_input = ''
while n > 0:
    user_input = input()
    str = ['rock','paper','scissors']
    computer_input = random.choice(str)
    winners = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
    if user_input == '!exit':
        print('Bye!')
        quit()
    elif user_input != '!exit' and user_input not in str:
        print('Invalid input')
    elif user_input == computer_input :
        print(f'There is a draw({user_input})')
    elif winners[user_input] == computer_input:
        print(f'Well done. Computer chose {computer_input} and failed')
    else:
        print(f'Sorry, but computer chose {computer_input}')
