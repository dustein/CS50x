import sys

if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)

if sys.argv[1].endswith(".py") == False:
    print("Not a Python file")
    sys.exit(1)

file_name = sys.argv[1]

try:
    with open(file_name) as file:
        data = file.readlines()
        count = 0
        for line in data:
            if line.lstrip().startswith("#") or line == "\n":
                pass
            else:
                count += 1
        print(count)
except FileNotFoundError:
    print("File does not exist")
    sys.exit(1)
