import random

number = random.randint(1, 10)

while True:
    guess = int(input("guess a number between 1 and 10: "))
    if guess > number:
        print("too high")
    elif guess < number:
        print("too low")
    else:
        break

print("Correct")