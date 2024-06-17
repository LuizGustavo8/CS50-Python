import sys
import requests

def main():


    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        current_price = response.json()["bpi"]["USD"]["rate_float"]

    except requests.RequestException:
        sys.exit()


    try:
        multiplicator = float(sys.argv[1])

    except IndexError:
        sys.exit("Missing command-line argument")
    except ValueError:
        sys.exit("Command-line argument is not a number")
    print(f"${multiplicator*current_price:,.4f}")

if __name__ == "__main__":
    main()

