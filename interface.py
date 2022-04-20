from simple_term_menu import TerminalMenu
#import animal
#set up animal with interactions
choice = "Play"

while(choice != "Quit"):
    options = ["Entry 1", "Entry 2", "Entry 3", "Quit"] #set the menu choices
    terminal_menu = TerminalMenu(options) #create the menu
    choice_num = terminal_menu.show() #user selects
    choice = options[choice_num] #save the user's choice
