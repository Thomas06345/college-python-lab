'''Author:Thomas Cherian
   date: 3-12-24
   python program:To find factorial using recursion'''
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
num1=int(input("enter number"))

ans=factorial(num1)
print(ans)