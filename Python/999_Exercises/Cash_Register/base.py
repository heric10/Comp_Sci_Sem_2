items = []
price = []
amount = int(input("How many items are you going to purchase? "))
for x in range(amount):
    name = input("What item are you going to purchase? ")
    cost = float(input("How many dollars does your item cost? "))
    print("You have just purchased "  +name)
    items.append(name)
    price.append(cost)
print("---------------")
print("Your receipt")
print("Thank you for shopping at EricMart!")
print("The following are the items you have purchased today: ")
for x in items:
    print(x)
print("Your total: " , end="")
total = 0
for x in price:
    total = total+x
print(total)