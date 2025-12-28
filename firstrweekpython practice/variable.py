#two item(variable) Discount price
item_name=input("enter item name: ")
price= float(input("enter item price: "))
discount = 0.55 #15% discount
Final_price=price-(price*discount)
print("\n.....bill Details...")
print(f"item Name: {item_name}")
print(f"Orginal price: ${price}")
print(f"Final Price: ${Final_price}")
