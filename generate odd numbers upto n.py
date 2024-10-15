'''Author:Thomas Cherian
   date: 15-10-24
   python program:to generate odd numbers up to n'''
limit=int(input("enter the limits:"))
odd_number=1
while odd_number<=limit:
    print(odd_number,"\t",end=" ")
    odd_number+=2
