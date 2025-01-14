# pip install inflect
import inflect

p = inflect.engine()

def main():
    names = []
    while True:
        try:
            name = input("Name: ").strip()
            names.append(name)
        except EOFError:
            print(f"\nAdieu, adieu, to {p.join(names)}")
            return

main()
