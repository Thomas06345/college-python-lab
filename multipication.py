'''Author:Thomas Cherian
   date: 29-10-24
   python program:To create a multipication table of given number up to 12.'''
num=int(input("enter your number"))
product=0
for i in range(1,13):
    product=num*i
    print(f'{num}*{i}={product}')
