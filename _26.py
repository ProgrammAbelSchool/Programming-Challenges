vowels = ["a", "e", "i", "o", "u"]

word = input("enter a word: ")

if word[0] in vowels:
    translated_word = word + "way"
else:
    translated_word = word[1:] + word[0] + "ay"

print(translated_word.lower())