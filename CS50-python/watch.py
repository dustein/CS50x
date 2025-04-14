import re
import sys

# Assume that the value of src will be surrounded by double quotes.
# And assume that the input will contain no more than one such URL.
# If the input does not contain any such URL at all, return None.

def main():
    print(parse(input("HTML: ")))

def parse(url):
    padrao = r'iframe src="(?:https?://)?(?:www\.)?youtube\.com/embed/([^"]+)"'
    busca = re.search(padrao, url )
    if not busca:
        return "None"

    return f"https://youtu.be/{busca.group(1)}"

if __name__ == "__main__":
    main()
