#get value from 
expression = input("Expression: ")

#split function to 3 part, x the left number, y the math syntex, z the right number
x, y, z = expression.split(" ")

#change to float
new_x = float(x)
new_z = float(z)

#計算
if y=="+":
    ans = new_x + new_z
elif y=="-":
    ans = new_x - new_z
elif y=="*":
    ans = new_x * new_z
elif y=="/":
    ans = new_x / new_z
#round取小數點幾位,1指小數點一位
print(round(ans , 1))
