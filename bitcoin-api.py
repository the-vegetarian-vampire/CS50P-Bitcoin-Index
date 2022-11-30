import requests
import sys
import json

if len(sys.argv) <= 1:
        sys.exit("Missing command-line argument")
else:
    try:
        # Command-line argument as an integer [float]
        bitcoin = float(sys.argv[1])
    except:
        sys.exit("Command-line argument is not a number")

try:
    # Queries coindesk's API for current Bitcoin price
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response = r.json()
    # Goes inside JSON dictionary and accesses price
    price = response["bpi"]["USD"]["rate_float"]
    # Takes API's current price and multiplies it by command-line argument value: 'bitcoin' variable on line 10.
    total = price * bitcoin
    print(f"${total:,.4f}")

except requests.RequestException:
    sys.exit("Request Failed")
