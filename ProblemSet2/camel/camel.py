#一如往常給input
get = input("camelCase: ")

#輸出最後結果
print("snake_case: " , end="")

#開始迭代每個字元"i"在input中
for i in get:
    #如果遇到"i"字元isupper，則印出"_"+該字元變小寫
    if i.isupper():
        print("_"+i.lower() , end="")
    #若沒有大寫，就逐字打印出來
    else:
        print(i , end="")

#回到最上面print出最後結果
print()

#for get.capitalize() in get:
#    first = get.capitalize().split()[0]
#    second = get.capitalize().split()[-1]
#    print(first + "_" + second)
