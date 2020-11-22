first_line = input("enter the first line of a nursery rhyme: ")

print(f"length of the line: {len(first_line)}")

start = int(input("enter starting number: ")) - 1
end = int(input("enter ending number: "))

print(f"{first_line[start:end]}")
