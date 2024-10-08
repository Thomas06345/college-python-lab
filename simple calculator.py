'''Author:Thomas Cherian
   date: 8-10-24
   python program:to print basic 5 arithemetic operations '''
num1=int(input("enter number 1:"))
num2=int(input("enter number 2:"))
num3=int(input("enter number 3:"))
addition=num1+num2
susbstraction=num2-num1
multipication=num1*num2
division=num1/num2
modulus=num1%num2
arithmetic=(num1+num2)*num3/2
print("The sum of",num1,"and",num2,"is:",addition)
print("The difference when",num2,"is substracted from",num2,"is:",susbstraction)
print("The product of",num1,"and",num2,"is:",multipication)
print("The quotient of",num1,"and",num2,"is :",division)
print("The remainder when",num1,"is divided by",num2,"is:",modulus)
print("The result of","(",num1,"+",num2,")*",num3,"/2 is:",arithmetic)