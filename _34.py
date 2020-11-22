print("""
1) Square
2) Triangle
""")
number = int(input("Enter a number: "))

if number == 1:
    side_length = int(input("Enter the length of one of its sides: "))
    print(f"Area = {side_length * side_length}")
elif number == 2:
    base = int(input("enter base length: "))
    height = int(input("enter height: "))
    area = (base * height) / 2
    print(f"Area = {area}")