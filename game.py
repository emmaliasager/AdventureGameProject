#Emmalia Sager
#Adventure Functions
#10/20/24

"""
game.py

This file imports the gamefunctions module and demonstrates usage of its functions.

Functions:
    run_game(): Starts the game by calling the imported functions and interating with the user.
"""

import gamefunctions

def run_game():
    """
    Runs the game by calling functions from gamefunctions and interacting with the user.

    Returns none
    """
    name = input("Enter your name: ")
    gamefunctions.print_welcome(name)

    gamefunctions.print_shop_menu("Ramen", 2, "Fig bar", 5)

    quantity, remaining_money = gamefunctions.purchase_item(50, 100, 2)
    print(f"Quantity purchased: {quantity}, Money left: {remaining_money}")

    monster = gamefunctions.new_random_monster()
    print(f"A wild {monster['Name']} appears! Health: {monster['Health']}")

if __name__ == "__main__":
    run_game()
    
