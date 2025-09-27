total_price = 0
number_of_items = int(input("Enter number of items: "))
while number_of_items < 0:
    print("Invalid item number, please re-enter")
    number_of_items = int(input("Enter number of items: "))
for items in range(number_of_items):
    item_price = float(input("Enter item price: "))
    total_price = total_price + item_price
if total_price > 100:
    total_price = total_price - total_price * 0.1
print(f"Total price for {number_of_items} is: ${total_price:.2f}")