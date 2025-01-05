frase = input("Input: ").strip()
for letter in frase:
    if letter in ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]:
        print("", end="")
    else:
        print(letter, end="")
print()
