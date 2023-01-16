import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess > random_number:
            print('High, Guess Lower')
        elif guess < random_number:
            print('Low, Guess Higher')
    print(f"You are right, matey! The number was indeed {random_number}.")

guess(5)