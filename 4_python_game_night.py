#Task 1: Random Choice Game
import random

game = ['1','2','3','4','5','6']

while True:
    my_choice = input('Guess a number between 1-6: ')
    computer = random.choice(game)
    print('The correct guess is: ', computer)
    win = input('Did you win? yes or no: ')
    if win == 'yes':
        print('Congratulations, you win!')
        break