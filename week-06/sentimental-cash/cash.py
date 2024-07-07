from cs50 import get_float

troco = -1

while (troco < 0):
    troco = get_float("Change: ")

moedas = 0
contador = 0

if (troco > 0.25):
    moedas = int(troco / 0.25)
    contador += moedas
    troco = round((troco - (moedas * 0.25)), 2)
if (troco >= 0.10):
    moedas = int(troco / 0.10)
    contador += moedas
    troco = round((troco - (moedas * 0.10)), 2)
if (troco >= 0.05):
    moedas = int(troco / 0.05)
    contador += moedas
    troco = round((troco - (moedas * 0.05)), 2)
if (troco < 0.05):
    moedas = int(troco / 0.01)
    contador += moedas

print(contador)
