import random
user_input = str(input())
str = ['rock','paper','scissors']
computer_input = random.choice(str)
winners = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}

if user_input == computer_input :
    print(f'There is a draw({user_input})')
elif winners[user_input] == computer_input:
    print(f'Well done. Computer chose {computer_input} and failed')
else:
    print(f'Sorry, but computer chose {computer_input}')
