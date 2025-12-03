from datetime import date
from operator import sub
import sys
import inflect


def main():
    try:
        date_of_birth = date.fromisoformat(input("Date of birth: "))
        convert_minutes(date_of_birth)
    except:
        sys.exit("Invalid date")


def convert_minutes(date):
    p = inflect.engine()
    today = date.today()
    time_delta = sub(today, date)
    time_delta_days = time_delta.days
    time_delta_minutes = time_delta_days * 1440
    resp = p.number_to_words(time_delta_minutes, wantlist=False).replace(" and ", " ")
    resp_final = (f"{resp.capitalize()} minutes")
    print(resp_final)
    return resp_final


def validate_date(date_str):
    try:
        return date.fromisoformat(date_str)
    except ValueError:
        raise ValueError("Invalid date format")


if __name__ == "__main__":
    main()

