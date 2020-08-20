#build a game run from terminal to guess a number
# must include sys.argv

import sys
import random


#Creating the base for the game
low = 1
high = 10

while True:
    try:
        name = sys.argv[1]
        low = int(sys.argv[2])
        high = int(sys.argv[3])
        print('set from cmd')
        break
    except IndexError:
        name = input("What is your name?  ")
        break

answer = random.randint(low, high)

print(f'Hello {name}.')
while True:
    guess = int(input(f'Please guess a number between {low} and {high}: '))
    if guess != answer:
        print(f'That is not correct')
    elif guess == answer:
        print(f"Congratulations {name}! You got it!")
        break
    elif guess > high or guess < low:
        print(f' Your guess should be between {high} and {low}')