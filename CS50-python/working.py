import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    padrao = r"^(?:([0-9]|1[0-2])(?::[0-5][0-9])?\s?(AM|PM))\s?to\s?(?:([0-9]|1[0-2])(?::[0-5][0-9])?\s?(AM|PM))$"

    try:
        timeGiven = re.search(padrao, s)
        if timeGiven == None:
            raise ValueError

        timeNew = s[:00]
        print(timeNew)
    except ValueError:
        return 1

    return timeGiven


...


if __name__ == "__main__":
    main()
