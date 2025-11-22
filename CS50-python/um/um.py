import re
import sys


def main():
    print(count(input("Text: ")))

def count(s):
    matches = re.findall(r'\bum\b', s, re.IGNORECASE)
    # counter = 0
    # for um in matches:
    #     counter += 1
    #     # print(counter)

    # return counter

    return len(matches)




if __name__ == "__main__":
    main()
