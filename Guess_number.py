import numpy as np

print("Welcome to the Number Guesser where you guess a number from a range of your choice")
name = input("Before we start, please type your name: ")

lower = int(input(f"Hi, {name}. Please put a number where we start: "))
higher = int(input(f"Please put the higher bound of the range: "))

while higher < lower:
    higher = int(input(f"Please put a number higher than {lower}: "))

print(f"Nice! I am thinking of a number from {lower} to {higher}.")
answer = np.random.randint(lower, higher)

guess = int(input("What is the number? "))

while guess != answer:
    if guess < answer:
        guess = int(input("Too low. Please guess again. "))
    else: 
        guess = int(input("Too high. Please guess again. "))

restart = input(f"Great work, {name}.")