from simple_term_menu import TerminalMenu
from pet import Pet  #import Pet class
my_pet = Pet() #create the pet

choice_num = 0

while(choice_num != 3):
    options = ["Name your pet", "Entry 2", "Entry 3", "Quit"] #set the menu choices
    terminal_menu = TerminalMenu(options) #create the menu
    choice_num = terminal_menu.show() #user selects

    if choice_num == 0:
        print("-"*30) #print a line
        print("What would you like to name your pet?") #print the prompt
        name = input(">>> ") #get the user input
        my_pet.set_name(name) #set the pet's name
        print("-"*30) #print a line

    elif choice_num == 1:
        #Replace this with your own code
        print("You chose", options[choice_num])

    elif choice_num == 2:
        #Replace this with your own code
        print("You chose", options[choice_num])

print("Goodbye")
