from random import choice

guessed_side = input("heads (h) or tails (t): ")
actual_side = choice(["h", "t"])

if guessed_side == actual_side:
    print("You win!")
else:
    print("bad luck...")