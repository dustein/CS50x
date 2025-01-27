import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        print("not a CSV file")

    menu = []

    try:
        with open(sys.argv[1]) as csvfile:
            reader = csv.DictReader(csvfile)

            for name, small, large in reader:
                menu.append({"name": name, "small": small, "large": large})
                # print(tabulate({row["Sicilian Pizza"], row["Large"], row["Small"]}, headers="firstrow"))

            for pizza in menu:
                print(f"{pizza['name']}")

    except(FileNotFoundError):
        print("filenotfou error")
        sys.exit(1)

if __name__ == "__main__":
    main()
