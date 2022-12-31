def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #...
    #最少2字元最多6字元組成 AND 首兩字是字母 AND 所有字元都是字母或數字組成(“No periods, spaces, or punctuation marks are allowed.”)條件下
    if 2 <= len(s) <= 6 and s[0:2].isalpha() and s.isalnum():

        #“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. 
        #The first number used cannot be a ‘0’.”
        #i迭代字串
        for i in s:
            #若i是數字(i.isdigit()；偵測到第一個數字啟動該條件)
            if i.isdigit():
                #給個索引來應用
                index = s.index(i)
                #之後到底都是數字，數字不能夾在中間 and 第一個數字不能為0
                if s[index:].isdigit() and int(i) != 0:
                    return True
                else:
                    return False
        #迭代都是
        return True

main()
