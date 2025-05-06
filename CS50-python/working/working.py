import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # padrao = r"^(?:([0-9]|1[0-2])(?::[0-5][0-9])?\s?(AM|PM))\s?to\s?(?:([0-9]|1[0-2])(?::[0-5][0-9])?\s?(AM|PM))$"
    # padrao = r"^((?:[0-9]|1[0-2])(?::[0-5][0-9])?\s?(?:AM|PM))\s?to\s?((?:[0-9]|1[0-2])(?::[0-5][0-9])?\s?(?:AM|PM))$"
    padrao = r"^(([0-9]|1[0-2])(?::([0-5][0-9]))?\s?([AP]M))\s?to\s?(([0-9]|1[0-2])(?::([0-5][0-9]))?\s?([AP]M))$"
    try:
        timeGiven = re.search(padrao, s)
        if timeGiven == None:
            raise ValueError

    except ValueError:
        return 1

    print(timeGiven.group(0))
    print("1:")
    print(timeGiven.group(1))
    print("2:")
    print(timeGiven.group(2))
    print("3:")
    print(timeGiven.group(3))
    print("4:")
    print(timeGiven.group(4))
    print("5:")
    print(timeGiven.group(5))
    print("6:")
    print(timeGiven.group(6))
    print("7:")
    print(timeGiven.group(7))
    print("8:")
    print(timeGiven.group(8))

    if minutos == None:
        minutos == "00"

    # am_pm = converted.group(3).upper()

    if am_pm == "AM":
        if hora == 12:
            hora_nova = 0
        else:
            hora_nova = hora
    # se for "PM"
    else:
        if hora != 12:
            nora_hora = hora + 12
        else:
            hora_nova = hora

    return f'{hora_nova}:{minutos}'


...


if __name__ == "__main__":
    main()
