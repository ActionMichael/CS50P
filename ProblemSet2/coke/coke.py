amount_due = 50

while amount_due > 0:
    print("Amount Due: " , amount_due)

    coin = int(input("Insert Coin: "))

    #if coin==25 or coin==10 or coin==5:(也可以)
    #[],list資料型態,也可以當索引
    if coin in [25 ,10 ,5]:
        amount_due -= coin

#當扣錢到負時(或0時也適用)，轉成正的(題目要求的)
Change_owed = abs(amount_due)

print("Change owed: " , Change_owed)
