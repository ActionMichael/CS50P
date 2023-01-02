import re
import sys



def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    #驗證數字的正則表達式集，驗證數字，https://www.twblogs.net/a/5b8c343d2b7177188331474a
    if re.search("^([0-9]{1,3})+\.([0-9]{1,3})+\.([0-9]{1,3})+\.([0-9]{1,3})+$" , ip):
        listofnumber = ip.split(".")
        for number in listofnumber:
            #TypeError: '<' not supported between instances of 'str' and 'int'；所以number改型態為int
            if int(number)<0 or int(number)>255:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()
