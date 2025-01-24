import sys

def main():
    data = input("Fraction: ")
    percent = convert(data)
    print(gauge(percent))

def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            fuel = int(x)/int(y)
            if int(x) > int(y):
                pass
            else:
                return int(fuel*100)

        except (ZeroDivisionError, ValueError):
            sys.exit(1)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage:.0f}%"


if __name__ == "__main__":
    main()
