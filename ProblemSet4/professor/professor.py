import random


def main():

    generate_integer(get_level())


def get_level():
    while True:
        level = input("Level: ")
        if level not in ["1" , "2" , "3"]:
            continue
        return level

def generate_integer(level):
    score = 0
    #Randomly generates ten (10) math problems[隨機製造10題模擬題]
    for i in range(10):
        #計算錯誤次數
        tries = 1
        #題目型態
        if level == "1":
            x = random.randint(0 , 9)
            y = random.randint(0 , 9)
        elif level == "2":
            x = random.randint(10 , 99)
            y = random.randint(10 , 99)
        else:
            x = random.randint(100 , 999)
            y = random.randint(100 , 999)

        while True:
            print(f"{x} + {y} = " , end="")
            ans = input()
            #答對
            if ans == str(x+y):
                score += 1
                break
            #答錯，同一題錯3次內
            elif ans != str(x+y) and tries != 3:
                print("EEE")
                tries += 1
                continue
            #答錯，同一題超過3次錯
            else:
                print("EEE")
                print(f"{x} + {y} = {x+y}")
                break
    print("Score: " , score)

if __name__ == "__main__":
    main()
