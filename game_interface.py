################################
# interface for the Pet object
# ----------
# it's up to you to finish it and customize it! 
################################

from pet import Pet                             # imports the Pet class from pet.py
from helpers import menu                        # import menu 
 

print("-"*36)
print("-- 🐶 Welcome to Pet Simulator 🐱 --")
print("-"*36,"\n")

print("🤔 What would you like to name your pet?")
name = input(">>> ")

my_pet = Pet()                                  #create the pet
my_pet.set_name(name)

print("-"*25)
print("{} is ready!".format(my_pet.name))
print("-"*25)

game_play = True

while game_play == True:
    options = ["Introduce", "Quit"] #set the menu choices

    option = menu(options)

    if option == 'Introduce':
        my_pet.introduce()

    elif option == 'Quit':
        game_play = False

print("-"*29)
print("--- Leaving Pet Simulator ---")
print("-"*29)
