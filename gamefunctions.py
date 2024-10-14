#Emmalia Sager
#Adventure Functions
#10/06/24

def purchase_item(itemPrice, startingMoney, quantityToPurchase=1):
    """ This function takes the price of an item, the amount of money you start with, and the
    quantity of items you want to purchase, and then returns how many items you are able
    to purchase and the amount of money you have leftover after the purchase """
    num_purchased = startingMoney // itemPrice
    leftover_money = (startingMoney - (itemPrice * quantityToPurchase))

    if leftover_money < 0:
        leftover_money = 0
        
    return (num_purchased, leftover_money)

num_purchased, leftover_money = purchase_item(1.23, 10, 3)
print("You are able to purchase:", num_purchased, "items.")
print(f"You have ${leftover_money:.2f} leftover.")

num_purchased, leftover_money = purchase_item(1.23, 2.01, 3)
print("You are able to purchase:", num_purchased, "items.")
print(f"You have ${leftover_money:.2f} leftover.")

num_purchased, leftover_money = purchase_item(3.41, 21.12)
print("You are able to purchase:", num_purchased, "items.")
print("You have ${} leftover.".format(leftover_money))

num_purchased, leftover_money = purchase_item(31.41, 21.12)
print("You are able to purchase:", num_purchased, "items.")
print("You have ${} leftover.".format(leftover_money))
print(end='\n')

import random

def new_random_monster():
    """This function uses random to choose a monster from a dictionary list and outputs
    the monster and all of its characteristics (where health, power, and money are
    randomized each time"""
    monsterTypes = [{"Name": "Goblin", "Description": "Playful little creature with floppy ears and a big nose who is always up to some goofy antics.",
                     "Health": [5, 10, 15], "Power": [3, 6, 9], "Money": [30, 35, 40]}, 

                    {"Name": "Vulture", "Description": "A blood-thirsty vulture circles its prey before it visciously attacks.",
                     "Health": [20, 30, 40], "Power": [10, 12, 14], "Money": [3, 7, 11]},

                    {"Name": "Fairy", "Description": "A cutesie fairy with shimmering wings flies through the woods, leaving a trail of pixie dust behind.",
                     "Health": [83, 97, 115], "Power": [6, 11, 18], "Money": [42, 59, 74]}]

    monster = random.choice(monsterTypes)
    monster["Health"] = random.choice(monster["Health"])
    monster["Power"] = random.choice(monster["Power"])
    monster["Money"] = random.choice(monster["Money"])

    return monster

monster = new_random_monster()
print(monster["Name"])
print(monster["Description"])
print("Health:", (monster["Health"]))
print("Power:", (monster["Power"]))
print("Money:", (monster["Money"]))
print(end='\n')

#documentation and strings – centered welcome message

def print_welcome(name, width=20):
    """This function will create a centered welcome message"""
    print(f"{'Hello, ' + name + '!':^{width}}")

print_welcome("Emmalia")
print_welcome("Fritz")
print_welcome("Moose")
print(end='\n')

#documentation and strings – shop menu

def print_shop_menu(item1Name, item1Price, item2Name, item2Price):
    print("/-----------------------\\")
    print(f"| {item1Name:<12} ${item1Price:>7.2f} |")
    print(f"| {item2Name:<12} ${item2Price:>7.2f} |")
    print("\\-----------------------/")

print_shop_menu("Apple", 31, "Pear", 1.234)
print_shop_menu("Egg", 0.23, "Bag of Oats", 12.34)
print_shop_menu("Orange", 2.5, "Banana", 0.75)
print(end='\n')

