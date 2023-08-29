import numpy as np

print("Hi! Please think of a number. I'll guess what it is.")

answer = int(input("What number are you thinking? Promise I'm not peeking."))

lower = int(input(f"First, let me know the range of numbers to guess. Give me the minimum: "))
higher = int(input(f"And the maximum: "))

guess = np.random.randint(lower, higher)
print(f"The number you are thinking is {guess}.")

check = input(f"Am I right? Please type \"Y\" if yes. Type \"-\" if lower. Type \"+\" if higher.")

while check != "Y":
    if check == "-":
        higher = guess
        guess = np.random.randint(lower, higher)
        print(f"The number you are thinking is {guess}.")

    else:
        lower = guess
        guess = np.random.randint(lower, higher)
        print(f"The number you are thinking is {guess}.")
    

    check = input(f"Am I right? Please type \"Y\" if yes. Type \"-\" if lower. Type \"+\" if higher.")

print(f"Yehey! too easy")