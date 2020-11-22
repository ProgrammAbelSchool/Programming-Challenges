name = input("enter your name: ")
number = int(input("enter a number: "))

if number < 10:
    for i in range(number):
        print(name)
else:
    for i in range(3):
        print("Too high")