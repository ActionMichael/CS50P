#創一個字典型態
grocery = {}

#loop forever
while True:
    try:
        #全大寫
        item = input().upper()
        #有重複數量加1
        if item in grocery:
            grocery[item] += 1
        #沒有就自己是第1個
        else:
            grocery[item] = 1
    except EOFError:
        #跌代所有在字典型態資料內所有東西(以key(商品名稱下去撈))
        for key in sorted(grocery.keys()):
            print(grocery[key] , key)
        break
"""
for key in sorted(grocery.keys()):
    若直接print沒有這一行則只會印出最後一行的內容
    而無法全部字典印出
    若for key in grocery.keys():
    :( input of "tortilla" and "sweet potato" yields "1 sweet potato 1 tortilla" expected "1 sweet potato...", not "1 tortilla\n1 ..."
"""
