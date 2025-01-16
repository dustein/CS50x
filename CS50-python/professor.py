from random import randrange

def main():

    level = get_level()
    score = 0

    for i in range(1,10):

        num1 = generate_integer(level)
        num2 = generate_integer(level)
        quest = num1 + num2

        count = 0
        while count < 3:
            try:
                resp = int(input(f"{num1} + {num2} = "))

            except ValueError:
                print("EEE")
                count += 1
                pass

            else:
                if resp == int(quest):
                    score += 1
                    break
                else:
                    print("EEE")
                    count += 1


    print(f"Score: {score}")
    return

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass

def generate_integer(n):
    if n == 1:
        number = randrange(0, 9)
    elif n == 2:
        number = randrange(10, 99)
    else:
        number = randrange(100, 999)

    return number


if __name__ == "__main__":
    main()
