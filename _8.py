bill = input("Total price of bill: ")
people = input("Number of people: ")

amount_per_person = float(bill) / float(people)

print(f"Each person has to pay {round(amount_per_person, 2)}")
