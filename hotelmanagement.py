# hotelmanagement
menu= {
    'Pizza':200,
    'Pasta':90,
    'Burger':80,
    'Coffee':110,
    'salad':80,
     
}
print(menu)

#Greed
print("Welcome to Our PYTHON Restaurant")
print("Pizza: Rs200\nPasta: Rs90\nBurger: Rs80\nCoffee: Rs110\nSalad: Rs80")

order_total = 0

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Ordered item{item_1} is not available yet!")
another_order = input("Do you want to add another item? (Yes/No)")

if another_order == "Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item{item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not available!")

    print(f"The total amount of items to pay is {order_total}")    

