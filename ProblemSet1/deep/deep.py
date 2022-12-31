ans = input("What is the Answer to the Great Question of Life, the Universe, and Everytion? ")

#condition = (ans.strip()=="42" or ans.lower().strip()=="forty-two" or ans.lower().strip()=="forty two")
#不能ans=="42" or "forty-two" or "forty two"會不管有沒有符合都yes；這點很怪

#if condition:
#have to say the name of the variable and the operator and when you use the operator you have to say again the variable and the operator that you want to compare 
#這就是為什麼"ans.strip()=="要重複這麼多次
if (ans.strip()=="42" or 
    ans.lower().strip()=="forty-two" or 
    ans.lower().strip()=="forty two"):
    #.lower()將ans內部字串轉成小寫.strip()預設刪除ans頭尾空格
    print("Yes")  
else:
    print("No")

"""
(法三)
if ans.strip()=="42":
    print("Yes")
elif ans.lower().strip()=="forty-two":
    print("Yes")
elif ans.lower().strip()=="forty two":
    print("Yes")
else:
    print("No")
"""


"""
用來去除頭尾字符、空白符(包括\n、\r、\t、' '，即：換行、回車、制表符、空格)

lstrip：用來去除開頭字符、空白符(包括\n、\r、\t、' '，即：換行、回車、制表符、空格)

rstrip：用來去除結尾字符、空白符(包括\n、\r、\t、' '，即：換行、回車、制表符、空格)

從字面可以看出r=right，l=left，strip、rstrip、lstrip是開發中常用的字符串格式化的方法。

注意：這些函數都只會刪除頭和尾的字符，中間的不會刪除。

>> name = '-# www.pythontab.com #-' 
>> name '-# www.pythontab.com #-' >>> name.strip('#-') #刪除開頭和結尾的#和-，空格被保留了 ' www.pythontab.com ' >>> 
>> name.lstrip('12') #刪除開頭的#和- ' www.pythontab.com #-' 
>> name.rstrip('12') #刪除結尾的#和- '-# www.pythontab.com '

"""
