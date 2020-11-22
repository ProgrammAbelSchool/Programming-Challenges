first_name = input("enter your first naem: ")

if len(first_name) < 5:
    last_name = input("enter your last naem: ")

    print((first_name + last_name).upper())
else:
    print(first_name.lower())