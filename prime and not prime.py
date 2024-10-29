'''Author:Thomas Cherian
   date: 29-10-24
   python program:to find if the given number is prime or not.'''
check_prime=int(input("enter a number"))
for i in range (2,(check_prime//2)+1):
    if check_prime % i==0:
        break
if i==check_prime//2:
    print(f"the given number {check_prime} is prime")
else:
    print(f"the given number {check_prime} is not prime")