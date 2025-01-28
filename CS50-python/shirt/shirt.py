import sys
import os
from PIL import Image

def main():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)

    img_in = sys.argv[1].lower()
    img_out = sys.argv[2].lower()
    if not img_in.endswith((".jpg", ".jpeg", ".png")) or not img_out.endswith((".jpg", ".jpeg", ".png")):
        print("Invalid input")
        sys.exit(1)
    # elif not img_in.split(".")[1] == img_out.split(".")[1]:
    elif not os.path.splitext(img_in)[1] == os.path.splitext(img_out)[1]:
        print("Input and output have different extensions")
        sys.exit(1)

    try:
        with Image.open(img_in) as image_in:
            ...

    except(FileNotFoundError):
        print("File not found")
        sys.exit(1)

if __name__ == "__main__":
    main()
