# import re
# import sys


# def main():
#     print(convert(input("Hours: ")))


# def convert(s):
#     padrao = r"^((0?[1-9]|1[0-2])(?::([0-5][0-9]))?\s?([AP]M))\s?to\s?((0?[1-9]|1[0-2])(?::([0-5][0-9]))?\s?([AP]M))$"
#     try:
#         timeGiven = re.search(padrao, s)
#         if timeGiven == None:
#             raise ValueError

#     except ValueError:
#         return 1

#     print("2:") # hora inicial
#     print(timeGiven.group(2))
#     hora_inicial = timeGiven.group(2)

#     print("3:") # minutos iniciais
#     print(timeGiven.group(3))
#     minutos_inicial = timeGiven.group(3)
#     if minutos_inicial == None:
#         minutos_inicial = 00

#     print("4:") # AM/PM
#     print(timeGiven.group(4))
#     am_pm_inicial = timeGiven.group(4).upper()

#     print("6:") # hora final
#     print(timeGiven.group(6))
#     hora_final = timeGiven.group(6)

#     print("7:") # minutos final
#     print(timeGiven.group(7))
#     minutos_final = timeGiven.group(7)
#     if minutos_final == None:
#         minutos_final = 00

#     print("8:") # AM/PM
#     print(timeGiven.group(8))
#     am_pm_final = timeGiven.group(8).upper()

#     if am_pm_final == "PM" and hora_final != 12:
#         hora_final += 12
#     elif am_pm_final == "AM" and hora_final == 12:
#         hora_final = 0

#     return f'{hora_final}:{minutos_final}'


# ...
# # 06:00 AM to 09:30 PM
# # 6:10 AM to 9:00 PM

# if __name__ == "__main__":
#     main()

import re
import sys

def main():

    try:
        time_input = input("Hours: ")
        print(convert(time_input))

    except ValueError:
        sys.exit("ValueError")


def convert(s):

    pattern = r"^(0?[1-9]|1[0-2])(?::([0-5][0-9]))?\s(AM|PM)\sto\s(0?[1-9]|1[0-2])(?::([0-5][0-9]))?\s(AM|PM)$"
    match = re.search(pattern, s, re.IGNORECASE)

    if not match:
        raise ValueError

    start_hour, start_min, start_ampm, end_hour, end_min, end_ampm = match.groups()

        # Hours: 9 AM to 5 PM
        # ('9', None, 'AM', '5', None, 'PM')

    start_hour_24 = converte_24(start_hour, start_ampm)
    end_hour_24 = converte_24(end_hour, end_ampm)

    start_min = start_min if start_min else "00"
    end_min = end_min if end_min else "00"

    return f'{start_hour_24}:{start_min} to {end_hour_24}:{end_min}'

def converte_24(hora, ampm):
    if ampm.upper() == "AM":
        return 0 if hora == 12 else hora
    else:
        return hora if hora == 12 else int(hora) + 12

if __name__ == "__main__":
    main()
