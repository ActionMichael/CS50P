import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

#Expects zero or two command-line arguments:

##Zero if the user would like to output text in a random font.
##len(sys.argv)是指"python figlet.py"的commender為"1"，除python外後面的字串有幾個，若1個則是random變形型態
if len(sys.argv)==1:
    randomfont = True
##Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, 
##and the second of the two should be the name of the font.
##其他len(sys.argv)是指"python figlet.py (-f or --font) xxx"為"3"，除python外後面的字串有幾個，若3個則是指定變形型態
elif len(sys.argv)==3 and (sys.argv[1]=="-f" or sys.argv[1]=="--font"):
    randomfont = False
##若len(sys.argv)為非1非3則結束
#sys.exit(0)和exit(1)；exit(0)：無錯誤退出；exit(1)：有錯誤退出
else:
    print("Invalid usage")
    sys.exit(1)


#msg = input("Input: ")測試用

#You can then get a list of available fonts with code like this:
figlet.getFonts()

#上述若指定變形型態(-f or --font)
if randomfont==False:
    try:
        #則指定的型態在"sys.argv[2]"，python figlet.py (-f or --font) xxx中的"xxx"
        figlet.setFont(font=sys.argv[2])
    #除非"sys.argv[2]"所輸入的指定型態不存在則...
    except:
        print("Invalid usage")
        sys.exit(1)
else:
    font = random.choice(figlet.getFonts())

msg = input("Input: ")

#print(f"Output: {figlet.renderText(msg)}")會出現破圖
print("Output:")
print(figlet.renderText(msg))

