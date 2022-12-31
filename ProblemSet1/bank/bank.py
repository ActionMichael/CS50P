"""
In a file called bank.py, implement a program that prompts the user for a greeting. 
If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20. 
Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.
"""

ans = input("Greeting: ")

if ans.lower().strip()=="":
    print("None")
#ans.lower()將ans字串全部轉成小寫,.strip()預設刪除ans頭尾空格
#.split(",")[0]=="hello"，用","所分隔出的第一字"word"等於hello
elif ans=="hello" or ans.lower().strip().split(",")[0]=="hello":
    print("$0")
#ans.lower將ans字串全部轉成小寫,.strip()預設刪除ans頭尾空格
#[0]指第一個"字元"character，前面不能加"."ans.lower().[0]=="h" SyntaxError: invalid syntax    
elif ans.lower().strip()[0]=="h":
    print("$20")
else:
    print("$100")
