import random

def main():

    number = get_level_num()
    print("NUMBER: ", number)
    guess = get_guess()

    while guess != number:
        if guess < number:
            print("Too small!")
            guess = get_guess()
        elif guess > number:
            print("Too large!")
            guess = get_guess()

    print("Just right!")
    return

def get_level_num():
    while True:
        try:
            level = int(input("Level: "))
            number = random.randint(1, level)
            return number

        except ValueError:
             print("erro de valor")
             pass

def get_guess():
    while True:
        try:
            guess = int(input("Guess: "))
            return guess
        except ValueError:
            print("valueerror")
            pass

if __name__ == "__main__":
    main()
