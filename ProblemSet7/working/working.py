import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    isclockformat = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$" , s)
    if isclockformat:
        pieces = isclockformat.groups()
        if int(pieces[1])>12 or int(pieces[5])>12:
            raise ValueError
        firsttime = newformat(pieces[1], pieces[2], pieces[3])
        secondtime = newformat(pieces[5], pieces[6], pieces[7])
        return firsttime + " to " + secondtime
        #return pieces
    else:
        raise ValueError

def newformat(hour , minute , ampm):
    if ampm == "PM":
        if int(hour) == 12:
            newhour = 12
        else:
            newhour = int(hour) + 12
    else:
        if int(hour) == 12:
            newhour = 0
        else:
            newhour = int(hour)
    
    if minute == None:
        newminute = ":00"
        newtime = f"{newhour:02}" + newminute
    else:
        newtime = f"{newhour:02}" + ":" + minute
    return newtime


if __name__ == "__main__":
    main()
