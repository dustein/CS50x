import sys
import csv

def main():

    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    elif not (sys.argv[1]).endswith(".csv"):
        print(f"Could not read {sys.argv[1]}")
        sys.exit(1)
    elif not (sys.argv[2]).endswith(".csv"):
        print(f"'{sys.argv[2]}' is not a valid file")
        sys.exit(1)

    # students = []

    try:
        with open(sys.argv[1]) as before, open(sys.argv[2], "w") as after:
            reader = csv.DictReader(before)
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(after, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                last, first = row['name'].split(',')
                writer.writerow(
                    {
                        "first": first.strip(),
                        "last": last,
                        "house": row["house"],
                    }
                )
                # # print(first, last)
                # students.append({"first": first.strip(), "last": last, "house": row["house"]})

    except(FileNotFoundError):
        print("arquivo nao encontrado")
        sys.exit(1)


if __name__ == "__main__":
    main()
