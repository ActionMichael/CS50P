def main():
    ans = input("What time is it? ")

    time = convert(ans)

    #have to say the name of the variable and the operator and when you use the operator you have to say again the variable and the operator that you want to compare 
    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")


def convert(time):
    hour , min = time.split(":")
    new_min = round(float(min)/60 , 2)
    return float(hour)+new_min


if __name__ == "__main__":
    main()
