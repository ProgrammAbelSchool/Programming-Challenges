people = int(input("number of people to invite to the party: "))

if people < 10:
    for i in range(people - 1):
        name = input("enter name: ")
        print(f"{name} has been invited")
else:
    print("Too many people")