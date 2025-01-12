import sys
import random
from pyfiglet import Figlet

f = Figlet()

fontes = f.getFonts()
fonte = "avatar"
f.setFont(font = fonte)

if len(sys.argv) == 1:
    f.setFont(font = random.choice(fontes))
    texto = input("Input: ")
    print(f"Output: \n{f.renderText(texto)}")
elif len(sys.argv) == 2:
    print("Invalid usage")
    sys.exit(1)
elif len(sys.argv) == 3:
    if (sys.argv[1] not in ["-f", "--font"]) or (sys.argv[2] not in fontes):
        print("Invalid usage")
        sys.exit(1)

    f.setFont(font = sys.argv[2])
    texto = input("Input: ")
    print(f"Output: \n{f.renderText(texto)}")

else:
    print("Invalid usage")
    sys.exit(1)
