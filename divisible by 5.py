'''Author:Thomas Cherian
   date: 15-10-24
   python program:to determine is a number is divisible by 5 '''
num=int(input("Enter a number "))
mode=num%5
if mode==0:
    print(num,"is divisible by 5")
else:
    print(num, "is not divisible by 5")
