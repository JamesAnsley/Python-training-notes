# build a game run from terminal to guess a number
# must include sys.argv
import sys
from random import randint

answer = randint(int(sys.argv[1]), int(sys.argv[2]))

while True:
    try:
        guess = int(input(f'Guess a number between {sys.argv[1]} and {sys.argv[2]}:  '))
        if (int(sys.argv[1]) - 1) < guess < (int(sys.argv[2]) + 1):
            if guess == answer:
                print('Way to go!')
                break
        else:
            print(f'HEY! I said between {sys.argv[1]} and {sys.argv[2]}')
    except ValueError:
        print('please enter a number')
        continue
