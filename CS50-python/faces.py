def main():
    frase = input("Give me a frase, and use emoticon for happy and sad...: ")
    print(convert(frase))

def convert(frase):
    return frase.replace(":)", "\N{slightly smiling face}").replace(":(", "\N{slightly frowning face}")

main()
