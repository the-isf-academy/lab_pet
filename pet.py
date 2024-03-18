# Pet class

class Pet:
    def __init__(self):
        '''This initializes the pet with its properties.'''

        self.name = None            # stores the pet's name as a string
        self.bored = False          # stores if the pet is bored 

    def set_name(self, name):
        '''This method sets the name property'''

        self.name = name

    def introduce(self):
        '''This method introduces the pet with its name.'''

        print(f"👋 Hi, I am {self.name}!")

    def play(self):
        '''If the pet is bored, then the pet will play. 
           If the pet just played, then it is not bored and doesn't want to play.
        '''

        if self.bored == False:          
            print("Wooooo, running!")
            self.bored = True          
        else:
            print("I don't want to play right now")
            self.bored = False 

