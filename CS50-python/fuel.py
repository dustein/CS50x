fracao = input("Fraction: ").strip()
x, a, y = fracao
try:
    int(x) / int(y) * 100
except:
    print("deu ruim")
    ValueError
