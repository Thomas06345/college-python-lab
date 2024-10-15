'''Author:Thomas Cherian
   date: 15-10-24
   python program:to determine discount based on purchased amount '''
purchased_amount=int(input("Enter the purchased amount:"))
if purchased_amount>500:
    discount=purchased_amount*0.2
    total=purchased_amount - discount
    print("total amount is",total)
elif purchased_amount>=200 and purchased_amount<=500:
    discount = purchased_amount * 0.1
    total = purchased_amount - discount
    print("total amount is",total)
else:
    print("total amount is",purchased_amount)
