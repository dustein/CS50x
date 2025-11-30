from validator_collection import checkers

def main():
    email = input("What is your email address? ")

    is_valid = checkers.is_email(email)

    if is_valid:
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
