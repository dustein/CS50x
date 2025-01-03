# .gif - image/gif
# .jpg - image/jpeg
# .jpeg - image/jpeg
# .png - image/png
# .pdf - application/pdf
# .txt - text/plain
# .zip - application/zip OU application/x-zip-compressed

arquivo = input("File name: ").strip().lower()
if (arquivo.endswith(".jpg") or arquivo.endswith(".jpeg")):
    print("image/jpeg")
elif arquivo.endswith(".gif"):
    print("image/gif")
elif arquivo.endswith(".png"):
    print("image/png")
elif arquivo.endswith(".pdf"):
    print("application/pdf")
elif arquivo.endswith(".txt"):
    print("text/plain")
elif arquivo.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
