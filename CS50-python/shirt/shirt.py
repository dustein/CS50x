import sys
import os
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        # print("Too few command-line arguments")
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        # print("Too many command-line arguments")
        sys.exit("Too many command-line arguments")

    img_in = sys.argv[1].lower()
    img_out = sys.argv[2].lower()
    if not img_in.endswith((".jpg", ".jpeg", ".png")) or not img_out.endswith((".jpg", ".jpeg", ".png")):
        # print("Invalid input")
        sys.exit("Invalid input")
    elif not os.path.splitext(img_in)[1] == os.path.splitext(img_out)[1]:
        print("Input and output have different extensions")
        sys.exit("Input and output have different extensions")

    try:
        with Image.open(img_in) as image_in, Image.open("./shirt.png") as shirt:
            # pega o tamanho da imagem
            get_size = shirt.size
            print(get_size)
            # redimensiona a shirt pro tamanho da imagem
            imagem = ImageOps.fit(image=image_in, size=get_size)
            # sobrepoe a shirt na imagem
            imagem.paste(im=shirt, mask=shirt)
            imagem.save(img_out)


    except(FileNotFoundError):
        # print("File not found")
        sys.exit("File not found")

if __name__ == "__main__":
    main()
