from datetime import date
from operator import sub
import sys
import inflect

def main():
    today = date.today()
    print(today)
    p = inflect.engine()

    try:
        date_of_birth = input("Date of birth: ")
        date_of_birth_formated = date.fromisoformat(date_of_birth)

        time_delta = sub(today, date_of_birth_formated)
        time_delta_days = time_delta.days
        time_delta_minutes = time_delta_days * 1440
        resp = p.number_to_words(time_delta_minutes, wantlist=False).replace(" and ", " ")
        resp_final = (f"{resp.capitalize()} minutes")
        print(resp_final)

    except:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()