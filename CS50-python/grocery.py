def main():
    lista = {}

    while True:
        try:
            add_item = input().upper().strip()
            if add_item in lista:
                lista[add_item] += 1
                # print(lista)
            else:
                lista[add_item] = 1
                # print(lista)

        except EOFError:
            for key, value in sorted(lista.items()):
                print(value, key)

            return

main()
