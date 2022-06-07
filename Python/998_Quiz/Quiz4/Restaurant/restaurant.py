import random

restaurants = ["McDonalds", "TacoBell", "Dominos"]

McDonaldsMenu = ["Travy Patty", "McNuggets", "French Fries"]
DominosMenu = ["Pizza", "LavaCake", "ChickenWings"]
TacoBellMenu = ["Taco", "Burrito", "Quesdilla"]

restaurantinput = input("What restaurant do you want? The options are: McDonalds, Dominos, or TacoBell")

if restaurantinput == "McDonalds":
    print("Suggested items")
    print(McDonaldsMenu[random.randrange(0,2)])
    McDonaldsMenuInput = input("What menu item do you want? The options are: Travy Patty, McNuggets, or French Fries")
    
if restaurantinput == "Dominos":
    print("Suggested items")
    print(DominosMenu[random.randrange(0,2)])
    DominosMenuInput = input("What menu item do you want? The options are: Pizza, LavaCake, or ChickenWings")
    
if restaurantinput == "TacoBell":
    print("Suggested items")
    print(TacoBellMenu[random.randrange(0,2)])
    TacoBellMenuInput = input("What menu item do you want? The options are: Taco, Burrito, or Quesdilla")