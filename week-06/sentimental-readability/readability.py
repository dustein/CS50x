from cs50 import get_string

frase = get_string("Text: ")

nao_letras = [" ", ",", ".", "!", "?", ";", "'"]
fim_sentencas = [".", "!", "?"]
letras = 0
palavras = 1
sentencas = 0

for letter in frase:
    if (letter not in nao_letras):
        letras += 1

for word in frase:
    if (word == " "):
        palavras += 1

for sentence in frase:
    if (sentence in fim_sentencas):
        sentencas += 1

L = (letras / palavras) * 100
S = (sentencas / palavras) * 100
formula = 0.0588 * L - 0.296 * S - 15.8

if (formula < 1):
    print("Before Grade 1")
elif (formula >= 16):
    print("Grade 16+")
else:
    print(f"Grade {round(formula)}")

# print(f"letras {letras}; palavras {palavras}, sentenca {sentencas}; formula {formula}")
