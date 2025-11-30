import re
import sys

def main():

    try:
        time_input = input("Hours: ")
        print(convert(time_input))

    except ValueError:
        sys.exit("ValueError")


def convert(s):

    pattern = r"^(\d{1,2})(?::(\d{1,2}))?\s(AM|PM)\sto\s(\d{1,2})(?::(\d{1,2}))?\s(AM|PM)$"
    match = re.search(pattern, s, re.IGNORECASE)

    if not match:
        raise ValueError


    start_hour, start_min, start_ampm, end_hour, end_min, end_ampm = match.groups()

    start_hour_int = int(start_hour)
    start_min_int = int(start_min) if start_min else 0
    end_hour_int = int(end_hour)
    end_min_int = int(end_min) if end_min else 0

    if not (1 <= start_hour_int <= 12):
        raise ValueError
    if not (0 <= start_min_int <= 59):
        raise ValueError
    if not (1 <= end_hour_int <= 12):
        raise ValueError
    if not (0 <= end_min_int <= 59):
        raise ValueError

    start_hour_24 = converte_24(start_hour_int, start_ampm)
    end_hour_24 = converte_24(end_hour_int, end_ampm)

    return f'{start_hour_24:02}:{start_min_int:02} to {end_hour_24:02}:{end_min_int:02}'

def converte_24(hora, ampm):
    if ampm.upper() == "AM":
        return 0 if hora == 12 else hora
    else:
        return hora if hora == 12 else int(hora) + 12

if __name__ == "__main__":
    main()
