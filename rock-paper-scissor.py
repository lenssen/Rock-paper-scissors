
import random
name = input('Enter your name:')
print(f'Hello, {name}')
def uinput():
    n = 1
    user_input = ''

    ratings = 0
    while n > 0:
        user_input = input()
        strr = ['rock','paper','scissors']
        computer_input = random.choice(strr)
        winners = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
        if user_input == '!exit':
            print('Bye!')
            break
        elif user_input == '!rating':
            print(ratings)
        elif user_input != '!exit' and user_input not in strr:
            print('Invalid input')
        elif user_input == computer_input :
            print(f'There is a draw({user_input})')
            ratings += 50
        elif winners[user_input] == computer_input:
            print(f'Well done. Computer chose {computer_input} and failed')
            ratings += 100
        else:
            print(f'Sorry, but computer chose {computer_input}')
    return ratings

def filewriting():
    new_ratings = uinput()
    num =''
    with open('ratings.txt') as myfile:
        filedata = myfile.read()
        if name in filedata:
            file = open('ratings.txt','r')

            content = file.readlines()
            for line in content:
                if name in line:
                    for i in line:
                        if i.isdigit() == True:
                            num += i
            new_ratings += int(num)
            print(new_ratings)
            filedata = filedata.replace(num,str(new_ratings))
            with open('ratings.txt','w') as myfile:
                myfile.write(filedata)

        else:
            file = open('ratings.txt','a')
            file.write(name+' ')
            file.write(str(new_ratings)+'\n')
    file.close()

print(filewriting())
