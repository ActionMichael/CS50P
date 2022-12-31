#要求不符合條件下一直問
while True:
    #拿取訊息從外界輸入
    get = input("Fraction: ")
    #接下去要用
    index = get.find("/")
    try:
        #從開始，一直到index前結束的元素
        fwd = int(get[:index])
        #從index+1開始，一直到結束的元素
        aft = int(get[index+1:])
        function = fwd / aft
        if fwd > aft:
            continue
        break
    
    except (ValueError , ZeroDivisionError):
        continue

percent = round(function * 100)#取整數，小數第一位四捨五入

#if 99% or more remains, output F
if function >= 0.99:
    print("F")
#If, though, 1% or less remains, output E    
elif function <= 0.01:
    print("E")
else:
    print(str(percent)+"%")
