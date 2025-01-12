def main():

    gauge = get_fuel()
    percent = gauge*100
    if percent <= 1:
        print("E")
    elif percent >= 99:
        print("F")
    else:
        print(f"{percent:.0f}%")

def get_fuel():

    while True:
        try:
            data = input("Fraction: ")
            x, y = data.split("/")

            # print("Dados: ", x, y)
            fuel = float(int(x)/int(y))
            # print("fuel: ", fuel)
            if int(x) > int(y):
                pass
            else:
                return fuel

        except (ValueError, ZeroDivisionError):
            pass

main()
