'''Author:Thomas Cherian
   date: 15-10-24
   python program:to determine the smallest of three numbers '''
num1=int(input("enter number 1:"))
num2=int(input("enter number 2:"))
num3=int(input("enter number 3:"))
if num1<num2 and num1<num3:
    print(num1,"is the smallest number")
elif num2<num1 and num2<num3:
    print(num2,"is the smallest number")
else:
    print(num3,"is the smallest number")