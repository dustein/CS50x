import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # padrao = r"^(?:([0-9]|1[0-2])(?::[0-5][0-9])?\s?(AM|PM))\s?to\s?(?:([0-9]|1[0-2])(?::[0-5][0-9])?\s?(AM|PM))$"
    # padrao = r"^((?:[0-9]|1[0-2])(?::[0-5][0-9])?\s?(?:AM|PM))\s?to\s?((?:[0-9]|1[0-2])(?::[0-5][0-9])?\s?(?:AM|PM))$"
    # padrao = r"^(([0-9]|1[0-2])(?::([0-5][0-9]))?\s?([AP]M))\s?to\s?(([0-9]|1[0-2])(?::([0-5][0-9]))?\s?([AP]M))$"
    padrao = r"^((0?[1-9]|1[0-2])(?::([0-5][0-9]))?\s?([AP]M))\s?to\s?((0?[1-9]|1[0-2])(?::([0-5][0-9]))?\s?([AP]M))$"
    try:
        timeGiven = re.search(padrao, s)
        if timeGiven == None:
            raise ValueError

    except ValueError:
        return 1

    print("2:") # hora inicial
    print(timeGiven.group(2))
    hora_inicial = timeGiven.group(2)

    print("3:") # minutos iniciais
    print(timeGiven.group(3))
    minutos_inicial = timeGiven.group(3)

    print("4:") # AM/PM
    print(timeGiven.group(4))
    am_pm_inicial = timeGiven.group(4).upper()

    print("6:") # hora final
    print(timeGiven.group(6))

    hora_final = timeGiven.group(6)
    print("7:") # minutos final
    print(timeGiven.group(7))

    minutos_final = timeGiven.group(7)
    print("8:") # AM/PM
    print(timeGiven.group(8))
    am_pm_final = timeGiven.group(8).upper()

    if minutos_inicial == None or minutos_final == None:
        novo_minutos = "00"
        print(novo_minutos)

    if am_pm_inicial == "AM" or am_pm_final == "AM":
        if hora_inicial == 12:
            hora_inicial_nova = 0
        else:
            hora_inicial_nova = hora_inicial
            
    # se for "PM"
    else:
        if hora != 12:
            nora_hora = hora + 12
        else:
            hora_nova = hora

    return f'{hora_nova}:{minutos}'


...
# 06:00 AM to 09:30 PM
# 6:10 AM to 9:00 PM

if __name__ == "__main__":
    main()
