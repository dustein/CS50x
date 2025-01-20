import sys


def main():

    if 1 > argv > 2:
        print("falta argv ou tem demais")
    try:
        coins = float(argv[1])
    except ValueError:
        print("Comand-line argument is not a number")
        pass


if __name__ == "__main__":
    main()
