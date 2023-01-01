#https://api.coindesk.com/v1/bpi/currentprice.json
import requests
import sys
import json

if len(sys.argv) != 2:
    print("Missing command-line argument")
else:
    request = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    #print(json.dumps(request.json() , indent=2))----for good looking data inside---- (獲取到需要的資訊)

    try:
        float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    data = request.json()
    price = data["bpi"]["USD"]["rate"]
    #print(float(price)*2)：Traceback (most recent call last):ValueError: could not convert string to float: '23,038.6226'
    price = price.replace("," , "")#(資料預整理，將資料內","消除後才能轉換浮點數)
    amount = float(price) * float(sys.argv[1])
    print(f"${amount:,.4f}")


