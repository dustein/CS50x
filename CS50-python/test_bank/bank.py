def main():
    frase = input("Greeting: ").lower().strip()
    print(f"${value(frase)}")

def value(greeting):

    if (greeting.startswith("hello ") or greeting.startswith("hello")):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
