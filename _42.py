total = 0

for i in range(5):
    number = int(input("enter a number: "))
    included = input("do you want this to be included? ")

    if included.lower() == "yes":
        total += number

print(total)