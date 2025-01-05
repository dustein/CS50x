word = input("camelCase: ").strip()

for letter in word:
    if letter.isupper():
        print("_", letter.lower(), sep="", end="")
    else:
        print(letter, end="")

print()
