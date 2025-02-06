import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if sys.argv[1].endswith(".py") == False:
    sys.exit("Not a Python file")

file_name = sys.argv[1]

try:
    with open(file_name) as file:
        data = file.readlines()
        count = 0
        for line in data:
            # count = sum(1 for line in data if not (line.lstrip().startswith("#") or line.strip() == ""))
            if line.lstrip().startswith("#") or line.lstrip() == "":
                pass
            else:
                count += 1
        print(count)
except FileNotFoundError:
    sys.exit("File does not exist")
    
