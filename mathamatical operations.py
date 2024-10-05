'''Author:Thomas Cherian
   date: 5-10-24
   python program:t print square factorial and rasised to 2 the nuber inputed '''
import math
number=int(input("Enter a number:"))
sqrt=math.sqrt(number)
factorial=math.factorial(number)
raised=math.pow(number,2)
print("Square root of",number,":",sqrt)
print("Factorial of",number,":",factorial)
print(number,"raised to power 2:",raised)