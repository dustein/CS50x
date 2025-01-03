expression = input("Yor expression to calculate: ")
x, y, z = expression.split(" ")

if y == "+":
    result = int(x) + int(z)
    print(f"{result:.1f}")
elif y == "-":
    result = float(x) - float(z)
    print(result)
elif y == "*":
    print(float(x) * float(z))
elif y == "/":
    print(float(x) / float(z))
else:
    print("Error... invalid expression")
