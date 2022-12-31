#一如往常給input
get = input("Input: ")

#輸出最後結果
print("Output: " , end="")

#開始迭代每個字元"i"在input中
for i in get:
    #如果"i"字元不是母音印出
    if i.lower() not in ["a", "e", "i", "o", "u"] :
        print(i , end="")

#回到最上面print出最後結果
print()
