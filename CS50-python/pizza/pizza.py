import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif not sys.argv[1].endswith(".csv"):
        print("not a CSV file")
        sys.exit(1)

    menu = []

    try:
        with open(sys.argv[1]) as csvfile:
            reader = csv.reader(csvfile)

            for row in reader:
                menu.append(row)

    except(FileNotFoundError):
        print("filenotfou error")
        sys.exit(1)

    print(tabulate(menu, headers='firstrow', tablefmt="grid"))

if __name__ == "__main__":
    main()
