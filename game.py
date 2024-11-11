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
    load_choice = input("Would you like to (1) Start a New Game or (2) Load a Previous Game?")
    if load_choice == '2':
        file_name = input("Enter the filename of the saved game: ")
        game_data = gamefunctions.load_game(filename)
        if game_data:
            current_hp = game_data["hp"]
            current_gold = game_data["gold"]
            inventory = game_data["inventory"]
        else:
            print("Starting a new game.")
            current_hp, current_gold, inventory = 50, 15, []
    else:
        current_hp, current_gold, inventory = 50, 15, []
    
    #name = input("Enter your name: ")
    #gamefunctions.print_welcome(name)

    #current_hp = 50
    #current_gold = 15
    #inventory = []

    while True:
        #display current stats and options
        print(f"\nCurrent HP: {current_hp}, Current Gold: {current_gold}")
        print("What would you like to do?")
        print("1) Fight Monster")
        print("2) Sleep (Restore HP for 5 Gold)")
        print("3) Shop (Purchase Items)")
        print("4) Equip Weapon")
        print("5) Quit")

        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            monster = gamefunctions.new_random_monster()
            current_hp = gamefunctions.fight_monster(current_hp, monster)
            if current_hp <= 0:
                print("You have been defeated!")
                break
        elif choice == '2':
            if current_gold >= 5:
                current_hp = gamefunctions.sleep(current_hp)
                current_gold -= 5
            else:
                print("Not enough gold to sleep.")
        elif choice == '3':
            item = gamefunctions.new_random_item()
            gamefunctions.print_shop_menu([item])
            current_gold, inventory = gamefunctions.purchase_item(item['name'], item['price'], inventory, current_gold)
        elif choice == '4':
            equipped_weapon = gamefunctions.equip_item(inventory)
        elif choice == '5':
            filename = input("Enter a filename to save the game: ")
            gamefunctions.save_game(filename, current_hp, current_gold, inventory)
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    run_game()
    
