number = int(input("enter a number between 1 and 12: "))

if 1 <= number <= 12:
    for num in range(1, 13):
        print(num * number)