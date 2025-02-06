import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("not a CSV file")

    menu = []

    try:
        with open(sys.argv[1]) as csvfile:
            reader = csv.reader(csvfile)

            for row in reader:
                menu.append(row)

    except(FileNotFoundError):
        sys.exit("file not found error")

    print(tabulate(menu, headers='firstrow', tablefmt="grid"))

if __name__ == "__main__":
    main()
