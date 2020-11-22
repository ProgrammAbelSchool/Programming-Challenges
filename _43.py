direction = input("do you want to count up or down? ")

if direction.lower() == "up":
    number = int(input("enter the top number: "))
    
    for i in range(1, number):
        print(i)
elif direction.lower() == "down":
    number = int(input("enter a number below 20: "))

    for i in range(20, number - 1, -1):
        print(i)