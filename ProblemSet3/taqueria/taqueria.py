d = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

#總價先歸零
totalprice= 0
while True:

    try:
        item = input("Item ").title()#將輸入的字串首字字元變大寫，方便比對清單
    except EOFError:
        print()
        break

    if item in d:
        totalprice += d[item]
        print("Total: $", f"{totalprice:.2f}", sep="")
        """
        print("Total: $"+totalprice)
        Traceback (most recent call last):
        File "taqueria.py", line 24, in <module>
            print("Total: $"+totalprice)
        TypeError: must be str, not float"""

