pounds = float(
    input("No. of pounds to take on holiday: ")
    )


euros = round(pounds * 1.09, 2)

print(f"You will have €{euros}")

notes = [(50, 0), (20, 0), (10, 0), (5, 0)]

for note, count in notes:
    if euros >= note:
        count = int(euros // note)
        euros -= note * count
        print(f"{note} notes - {count}")
