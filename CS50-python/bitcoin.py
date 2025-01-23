# pip install requests
import sys
import requests

def main():


    try:
        if len(sys.argv) != 2:
            print("Missing command-line argument")
            sys.exit(1)
        coins = float(sys.argv[1])

    except ValueError:
        print("Comand-line argument is not a number")
        sys.exit(1)

    try:
        dados = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
        rate = dados["bpi"]["USD"]["rate_float"]
        resposta = coins * rate

        print(f"${resposta:,.4f}")
    except requests.RequestException:
        pass

if __name__ == "__main__":
    main()
