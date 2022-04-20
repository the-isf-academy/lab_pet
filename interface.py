################################
# interface for the Pet object
# ----------
# it's up to you to finish it! 
# feel free to customize it as you please.
################################

# Creates a fancy menu system in the Terminal
from simple_term_menu import TerminalMenu

# Imports the Pet from pet.py
from pet import Pet  


def welcome():
    print("-"*35)
    print("---- Welcome to Pet Simulator ----")
    print("-"*35,"\n")

def get_name():
    print("What would you like to name your pet?")
    name = input(" > ")
    return name

def intro_game():
    print("Your pet is ready!")

def line_break():
    print("-"*25)

def end_game():
    print("\n")
    print("-"*29)
    print("--- Leaving Pet Simulator ---")
    print("-"*29)

def menu():
    '''This function creates an interactive Terminal menu.'''

    options = ["Introduce", "Quit"] #set the menu choices
    terminal_menu = TerminalMenu(options) #Creates the Terminal Menu 
    choice_num = terminal_menu.show() #Get user selected Option 

    return choice_num

def game_loop(my_pet):
    play = True

    while play == True:
        choice_num = menu()

        if choice_num == 0:
            my_pet.introduce()

        elif choice_num == 1:
            play = False

def main():
    welcome()
    name = get_name()

    my_pet = Pet() #create the pet
    my_pet.set_name(name)

    line_break()
    intro_game()
    line_break()

    game_loop(my_pet)

    end_game()


main()
