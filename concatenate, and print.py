'''Author:Thomas Cherian
   date: 8-10-24
   python program:to extract a concatenated sting'''
first_name=input("enter your first name")
last_name=input("enter your last name")
full_name=first_name+" "+last_name
print(full_name)
length=len(first_name)
extracted_first_name=full_name[:length]
print(extracted_first_name)