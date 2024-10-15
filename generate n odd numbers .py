'''Author:Thomas Cherian
   date: 15-10-24
   python program:to generate n odd numbers '''
limit=int(input("enter the limits:"))
odd_number=1
count=0
while count<limit:
    print(odd_number,"\t",end=" ")
    count+=1
    odd_number+=2
