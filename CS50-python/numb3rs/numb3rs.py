import re
import sys

def main():
    isTrue = validate(input("IPv4 Adress: "))
    print(isTrue)

def validate(ip):
    expression = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    result = re.search(expression, ip)
    if result:
        print("valido")
        return True
    else:
        return False

if __name__ == "__main__":
    main()
