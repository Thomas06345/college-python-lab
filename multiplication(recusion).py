'''Author:Thomas Cherian
   date: 3-12-24
   python program:To find product of two numbers using recursion'''
def multiply(n1,n2):
    if n2==1:
        return n1
    else:
        return n1+multiply(n1,n2-1)
num1=int(input("enter number1:"))
num2=int(input("enter number2:"))
print(multiply(num1,num2))
