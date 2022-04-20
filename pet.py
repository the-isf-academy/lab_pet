class Pet:
    def __init__(self):
        self.name = None #The pet's name
        self.tired = False #Tells us if the pet is tired
        self.bored = True #Tells us if the pet is bored

    def set_name(self, name):
        self.name = name #Saves the pet's new name

    def introduce(self):
        print("Hi, I'm", self.name)

    def play(self):
        if self.bored == True: #The pet will only play if it's bored
            print("Let's play!!!")
            self.bored = False #Now the pet isn't bored anymore
            self.tired = True #But it's tired
        else:
            print("I don't want to play right now")

    def nap(self):
        if self.tired == True: #The pet will only nap if it's tired
            print("Zzzzzzzzzzzz.........")
            self.tired = False #Now the pet isn't tired anymore
            self.bored = True #But it's bored
        else:
            print("I'm not tired!!!!!")
