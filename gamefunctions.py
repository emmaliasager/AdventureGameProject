#Emmalia Sager
#Adventure Functions
#10/06/24

"""
gamefunctions.py

This module contains various functions for a simple game, including functions to print a
welcome message, display a shop menu, handle purchasing items, and generate random monsters.

Functions:
    print_welcome(name, width=20): Prints a centered welcome message.
    print_shop_menu(item1Name, item1Price, item2Name, item2Price): Displays a shop menu.
    purchase_item(itemPrice, startingMoney, quantityToPurchase=1): Processes the purchase of an item.
    new_random_monster(): Generates a random monster with randomized attributes.
"""

import random

#documentation and strings – centered welcome message

def print_welcome(name, width=20):
    """
    This function prints a centered welcome message with names.

    Parameters:
        name: Person's name
        width: The width for centering the message (default is 20).

    Returns none
    """

    print(f"{'Hello, ' + name + '!':^{width}}")


#documentation and strings – shop menu

def print_shop_menu(item1Name, item1Price, item2Name, item2Price):
    """
    This function displays a shop menu with item names and corresponding prices.

    Parameters:
        item1Name: The name of the first item.
        item1Price: The price of the first item.
        item2Name: The name of the second item.
        item2Price: The price of the second item.

    Returns none
    """

    print("/-----------------------\\")
    print(f"| {item1Name:<12} ${item1Price:>7.2f} |")
    print(f"| {item2Name:<12} ${item2Price:>7.2f} |")
    print("\\-----------------------/")


    
def purchase_item(itemPrice, startingMoney, quantityToPurchase=1):
    """ This function calculates how many items can be purchased and returns the quantity purchased and remaining money

        Parameters:
        itemPrice: The price of a single item
        startingMoney: The amount of money available to spend
        quantityToPurchase: The desired quantity to purchase. The default value is 1.

        Returns a tuple containing the quantity purchased and the remaining money"""

    totalCost = itemPrice * quantityToPurchase

    if totalCost <= startingMoney:
        quantityPurchased = quantityToPurchase
        remainingMoney = startingMoney - totalCost
    else:
        quantityPurchased = int(startingMoney // itemPrice)
        remainingMoney = startingMoney - (quantityPurchased * itemPrice)

    return quantityPurchased, remainingMoney


def new_random_monster():
    """
    This function generates a random monster with randomized health, power, and money attributes.

    Returns a dictionary representing the randomly generated monster.
    """

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


def fight_monster(user_hp, monster):
    print(f"A wild {monster['Name']} appears! Health: {monster['Health']}, Power: {monster['Power']}")
    while True:
        damage_to_monster = random.randint(5, 10)
        damage_to_user = monster['Power']

        monster['Health'] -= damage_to_monster
        user_hp -= damage_to_user

        print(f"You dealth {damage_to_monster} damage to {monster['Name']}!")
        print(f"{monster['Name']} dealt {damage_to_user} to you!")

        if monster['Health'] <= 0:
            print(f"You have defeated the {monster['Name']}!")
            return user_hp
        elif user_hp <= 0:
            return user_hp

        fight_choice = input("What would you like to do? (1) Continue fighting (2) Run away: ")
        if fight_choice == '2':
            print("You ran away!")
            return user_hp

def sleep(current_hp):
    restored_hp = 10
    new_hp = min (current_hp + restored_hp, 30)
    print(f"You slept and restored {restored_hp} HP!")
    return new_hp

