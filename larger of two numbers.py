'''Author:Thomas Cherian
   date: 15-10-24
   python program:to determine the larger of two numbers '''
num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
if num1>num2:
    print(num1,"is the larger number")
elif num2>num1:
    print(num2,"is the larger number")
else:
    print ("Both the numbers are equal")