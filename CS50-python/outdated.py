meses = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        try:
            data = input("Date: ").strip()
            if "/" in data:
                mes, dia, ano = data.split("/")
                # if (int(mes) > 12 or int(dia) > 31 or len(ano) != 4):
                #     raise ValueError()
                # print(f"{ano}/{int(mes):02}/{int(dia):02}")
            else:
                mes, dia, ano = data.split(" ")
                if mes in meses:
                    mes = int(meses.index(mes)) + 1
                    dia = dia[:-1]

                    # print(f"{ano}/{meses.index(mes):02}/{int(dia[:-1]):02}")
                else:
                    raise ValueError()

            if (int(mes) > 12 or int(dia) > 31 or len(ano) != 4):
                    raise ValueError()

            print(f"{ano}-{int(mes):02}-{int(dia):02}")
            return

        except ValueError:
            pass

main()
