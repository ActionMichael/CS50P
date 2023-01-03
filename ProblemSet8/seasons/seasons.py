from datetime import date
import re
import sys
import inflect

p = inflect.engine()

def main():
    birthday = input("Date of Birth: ")
    try:
        year, month, day = checkbirthday(birthday)
    except:
        sys.exit("Invalid Date")
    dateofbirth = date(int(year), int(month), int(day))
    dateoftoday = date.today()
    diff = dateoftoday - dateofbirth
    diffbymin = diff.days*24*60
    ## CONVERT NUMERALS TO WORDS (i.e. 1->"one", 101->"one hundred and one", etc.) RETURNS A SINGLE STRING...
    # words = p.number_to_words(1234)
    output = p.number_to_words(diffbymin, andword="")
    #.capitalize()首字大寫
    print(output.capitalize() + " minutes")

def checkbirthday(birthday):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birthday):
        year, month, day = birthday.split("-")
        return year, month, day

if __name__ == "__main__":
    main()
