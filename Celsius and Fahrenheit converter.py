'''Author:Thomas Cherian
   date: 22-10-24
   python program:to convert temperature values back and forth between Celsius and Fahrenheit.'''
temperature=float(input("Enter temperature:"))
metric=input("Is this in Celsius(C) or Fahrenheit(F) ?")
if metric=="C":
    fahreheit=(9/5*temperature)+32
    print(fahreheit,"fahrenheit")
elif metric=="F":
    celsius=5/9*(temperature-32)
    print(celsius,"celsius")
else:
    print("invalid input")