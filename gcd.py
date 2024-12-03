'''Author:Thomas Cherian
   date: 3-12-24
   python program:To find greatest common denominator using recursion'''
def gcd(n1,n2):
    if n1%n2==0:
        return n2
    else:
        return gcd(n2,n1%n2)
num1=int(input("enter number1:"))
num2=int(input("enter number2:"))
print(gcd(num1,num2))