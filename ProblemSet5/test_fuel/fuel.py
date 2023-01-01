def main():
    #拿取訊息從外界輸入
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))

def convert(fraction):
    while True:
        #接下去要用
        index = fraction.find("/")
        try:
            #從開始，一直到index前結束的元素
            fwd = int(fraction[:index])
            #從index+1開始，一直到結束的元素
            aft = int(fraction[index+1:])
            function = fwd / aft
            if fwd > aft:
                fraction = input("Fraction: ")
                continue
            else:
                percentage = round(function * 100)#取整數，小數第一位四捨五入
                return percentage
    
        except (ValueError , ZeroDivisionError):
            continue

def gauge(percentage):
    #if 99% or more remains, output F
    if percentage >= 99:
        return "F"
    #If, though, 1% or less remains, output E    
    elif percentage <= 1:
        return "E"
    else:
        return str(percentage)+"%"

if __name__ == "__main__":
    main()
