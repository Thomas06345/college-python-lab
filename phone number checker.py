'''Author:Thomas Cherian
   date: 20-11-24
   python program:To check is a given mobile number is valid.'''
def mobile_no():
    num=input("enter mobile number:")
    if len(num)==10:
        if num[1]=="7" or num[1]=="8" or num[1]=="9":
            print("Valid")
        else:
            print("invalid")
    else:
        print("invalid")

mobile_no()