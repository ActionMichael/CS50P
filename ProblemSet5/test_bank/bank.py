def main():
    greeting = input("Greeting: ")
    value = value(greeting)
    print("$"+value)


def value(greeting):
    if greeting.lower().strip()=="":
        return None
    #ans.lower()將ans字串全部轉成小寫,.strip()預設刪除ans頭尾空格
    #.split(",")[0]=="hello"，用","所分隔出的第一字"word"等於hello
    elif greeting=="hello" or greeting.lower().strip().split(",")[0]=="hello":
        return 0
    #ans.lower將ans字串全部轉成小寫,.strip()預設刪除ans頭尾空格
    #[0]指第一個"字元"character，前面不能加"."ans.lower().[0]=="h" SyntaxError: invalid syntax    
    elif greeting.lower().strip()[0]=="h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
