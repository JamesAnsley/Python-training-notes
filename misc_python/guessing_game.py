# This game generates a random number from user inputs and asks the user to guess it

import sys
import random
import time

# check name from cmd
while True:
    try:
        user_name = sys.argv[1]
        print('set from cmd')
        print(f'Hello {user_name}')
        break
    except IndexError:
        user_name = input("Hello, welcome to the game. What is your name? ")
        time.sleep(2)
        print(f'Well {user_name} I hope you are ready...')
        time.sleep(2)
        break


def difficulty_menu():
    while True:
        difficulty = input("How hard do you want it? Easy, Medium, Hard, Brutal, or Custom:   ")
        if difficulty.lower() == 'easy':
            low = 0
            high = 10
            return low, high, difficulty

        elif difficulty.lower() == 'medium':
            low = 0
            high = 25
            return low, high, difficulty

        elif difficulty.lower() == 'hard':
            low = 0
            high = 50
            return low, high, difficulty

        elif difficulty.lower() == 'brutal':
            low = 0
            high = 50
            return low, high, difficulty

        elif difficulty.lower() == 'custom':
            low = int(input("What should the lowest possible number be?    "))
            high = int(input('What should the highest possible number be?    '))
            return low, high, difficulty

        else:
            print("select one of the options")


def penalty_wait():
    for i in range(10):
        print(f"{10 - i} seconds to wait")
        time.sleep(1)


guess_number = 0

while True:
    try:
        low = int(sys.argv[2])
        high = int(sys.argv[3])
        difficulty = 'custom'
        break
    except IndexError:
        low, high, difficulty = difficulty_menu()
        if difficulty.lower() == 'brutal':
            sleep = guess_number
            print(f"Oh. I forgot to mention. Since you picked {difficulty} there is a penalty for guessing poorly")
            time.sleep(1)
            print(f'Each wrong guess increases the wait between by half a second')
        break

# this sets the difficulty for the game
time.sleep(random.random() * 3)
print(f"I am picking a number between {low} and {high} inclusive...")
time.sleep(2)
print(f'Okay {user_name}. I have the number. Get to guessing.')
time.sleep(random.random() * 5)
guess_number = 0
sleep = 0

answer = random.randint(low, high)
print(answer)

while True:
    try:
        guess = int(input(f"Make your guess {user_name}: "))
        guess_number += 1
        time.sleep(.5)
        if guess == answer:
            if guess_number == 1:
                print(f'I guess you are psychic. Or lucky')
                time.sleep(.5)
                print("congratualations of getting it on the first guess")
                time.sleep(.5)
            else:
                print(f'CONGRATULATIONS!!! {user_name} it only took you {guess_number} attempts')
            print(f'Until next time {user_name}')
            break
        elif guess < low:
            print(
                f"{user_name} I said the answer is between {low} and {high} inclusive.)"
                f" Since you are rude you can wait.")
            guess_number += 1
            penalty_wait()
            if difficulty.lower() == 'brutal':
                time.sleep(guess_number / 2)
        elif guess > high:
            print(
                f"{user_name} I said the answer is between {low} and {high} inclusive. Since you are rude you can wait.")
            penalty_wait()
            guess_number += 1
            if difficulty.lower() == 'brutal':
                time.sleep(guess_number / 2)
        else:
            print("Hahahaha")
            time.sleep(.25)
            print("No")
            if difficulty.lower() == 'brutal':
                time.sleep(guess_number / 2)
    except ValueError:
        print("You must enter a number")
        print("Penalty time")
        guess_number += 1
        penalty_wait()
        continue
