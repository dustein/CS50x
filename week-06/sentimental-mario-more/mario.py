from cs50 import get_int

height = get_int("Height: ")
while (height > 8 or height < 1):
    height = get_int("Height: ")

for h in range(height):
    espaco = height - 1 - h
    tijolo = height - espaco
    print(f'{" " * espaco}{"#" * tijolo}')
