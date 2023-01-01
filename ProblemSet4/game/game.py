import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        continue

#randint(start, end)，(start, end): Both of them must be integer type values.
num = random.randint(1 , level)

#猜
while True:
    try:
        guess = int(input("Guess: "))
        
        if guess > num:
            print("Too large!")
        elif guess < num:
            print("Too small!")
        else:
            print("Just right!")
            break

    except ValueError:
        continue

