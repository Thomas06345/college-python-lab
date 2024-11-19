'''Author:Thomas Cherian
   date: 19-11-24
   python program:To show the item with highest stock value
   .'''
inventory =[
    ("laptop",10,60000.00),
    ("headphones",20,550.00),
    ("mouse",50,150.00),
    ("keyboard",20,200.00)
]
highest_stock_value=0
item_with_highest=None
for item in inventory:
    item_name,quantity,price=item
    stock_value = quantity*price
    print(f"Item name:{item_name},the stock value is: {stock_value}")
    if stock_value > highest_stock_value:
     highest_stock_value=stock_value
     item_with_highest = item_name
print(f"highest stock value is: {highest_stock_value}")
print(f"item with highest stock value is: {item_with_highest}")
