def main():
    time = input("What's time is it? ")
    value = convert(time)
    if 7 <= value <= 8:
        print("breakfast time")
    elif 12 <= value <= 13:
        print("lunch time")
    elif 18 <= value <= 19:
        print("dinner time")

def convert(time):
    hours, minute = time.split(":")
    if int(minute) != 0:
        minute = 1/(60/int(minute))
    return int(hours) + float(minute)


if __name__ == "__main__":
    main()
