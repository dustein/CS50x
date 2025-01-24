def main():
    frase = input("Input: ").strip()
    print(shorten(frase))

def shorten(word):
    vogais = "AaEeIiOoUu"
    nova = "".join(letter for letter in word if letter not in vogais)

    return nova

if __name__ == "__main__":
    main()
