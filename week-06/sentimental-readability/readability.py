from cs50 import get_string

frase = get_string("Text: ")

letras = 0
for letter in frase:
    print(letter)
    letras += 1

print(letras)
