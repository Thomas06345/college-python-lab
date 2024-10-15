'''Author:Thomas Cherian
   date: 15-10-24
   python program:to determine the fare based on age '''
age=int(input("Enter your age:"))
if age<10:
    print("fare is rupees 7")
elif age>=10 or age<60:
    print("fare is rupees 10")
else:
    print("fare is rupees 5")