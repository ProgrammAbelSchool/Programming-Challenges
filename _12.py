number1 = int(input("number 1: "))
number2 = int(input("number 2: "))

if number1 > number2:
    comparison = "greater than"
elif number1 < number2 :
    comparison = "less than"
else:
    comparison = "equal to"

print(number1, comparison, number2)