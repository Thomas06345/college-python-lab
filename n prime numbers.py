'''Author:Thomas Cherian
   date: 29-10-24
   python program:to find prime numbers upto n.'''
limit=int(input("enter a limit"))
for number in range(2,limit+1):
    isprime="true"
    for i in range(2,(number//2)+1):
        if number %i ==0:
            isprime="false"
            break
    if isprime=="true":
        print(number)