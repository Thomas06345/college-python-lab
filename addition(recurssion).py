'''Author:Thomas Cherian
   date: 3-12-24
   python program:To find sum of two numbers using recursion'''
def add(n1,n2):
    if n2==0:
        return n1
    else:
        return add(n1+1,n2-1)
num1=int(input("enter number1:"))
num2=int(input("enter number2:"))
ans=add(num1,num2)
print(ans)