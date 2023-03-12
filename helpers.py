# helper functions

from simple_term_menu import TerminalMenu       # creates a menu system in the Terminal


def menu(options):
    '''This function creates an interactive Terminal menu.
        takes a list as the parameter

        e.g. menu(['Play Game','quit'])
    '''

    terminal_menu = TerminalMenu(options)       # creates an instance of the TerminalMenu 
    option_num = terminal_menu.show()           # stores the user selected option 

    return options[option_num]