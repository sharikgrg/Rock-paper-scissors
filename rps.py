import random

answer = ''
while answer != 'no':
    answer = input('Rock,  Paper or Scissor: ')
    num = random.randint(1,3)
    if num == 1:
        num = 'rock'
    elif num == 2:
        num = 'paper'
    elif num == 3:
        num = 'scissor'

    if num == 'rock' and answer == 'rock':
        print(f'{num} draws with {answer}')
        print("it's a draw")

    elif num == 'paper' and answer == 'rock':
        print(f'{num} beats {answer}')
        print("you lost")

    elif num == 'scissor' and answer == 'rock':
        print(f'{num} loses against {answer}')
        print("yay, you won")

    elif num == 'scissor' and answer == 'scissor':
        print(f'{num} draws with {answer}')
        print("it's a draw")

    elif num == 'rock' and answer == 'scissor':
        print(f'{num} beats {answer}')
        print("you lost")

    elif num == 'paper' and answer == 'scissor':
        print(f'{num} loses against {answer}')
        print("yay, you won")

    elif num == 'paper' and answer == 'paper':
        print(f'{num} draws with {answer}')
        print("it's a draw")

    elif num == 'scissor' and answer == 'paper':
        print(f'{num} beats {answer}')
        print("you lost")

    elif num == 'rock' and answer == 'paper':
        print(f'{num} loses against {answer}')
        print("yay, you won")

else:
    print('Have a nice day')



