months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"]

while True:
    date = input("Date: ")

    if "/" in date:
        month , day , year = date.split("/")
    elif "," in date:
        date = date.replace("," , "")
        month , day , year = date.split(" ")
        if month in months:
            month = months.index(month) + 1

    try:
        #在"月","日"範圍外繼續詢問
        if int(month)>12 or int(day)>31:
            continue
        #其他在範圍內則切斷(while loop)並準備輸出結果print
        else:
            break
    #除非
    except ValueError:
        continue

print(f"{int(year)}-{int(month):02}-{int(day):02}")

