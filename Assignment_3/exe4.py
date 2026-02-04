import random

target = random.randint(1, 10)
guess = 0

while guess != target:
    guess = int(input("Guess a number: "))
    if guess > target:
        print("Too high")
    elif guess < target:
        print("Too low")
    else:
        print("Correct")
        