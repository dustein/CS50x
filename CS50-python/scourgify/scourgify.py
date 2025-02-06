import sys
import csv

def main():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    elif not (sys.argv[1]).endswith(".csv"):
        sys.exit(f"Could not read {sys.argv[1]}")

    elif not (sys.argv[2]).endswith(".csv"):
        sys.exit(f"'{sys.argv[2]}' is not a valid file")

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
        sys.exit("arquivo nao encontrado")


if __name__ == "__main__":
    main()
