'''Author:Thomas Cherian
   date: 19-11-24
   python program:To create a pattern using nested loop
   .'''
limit=int(input("enter the range:"))
print("first pattern is")
for i in range(1,limit+1):
	for j in range(i):
		print("*",end=" ")
	print()
print("second pattern is")
for i in range(limit,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()
print("third pattern is")
for i in range(1,limit+1):
    for j in range(limit-i):
        print( " ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()
print("fourth pattern is")
for i in range(limit,0,-1):
    for j in range(limit-i):
        print( " ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()