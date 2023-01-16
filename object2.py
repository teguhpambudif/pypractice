class PartyAnimal:
    # x is an littebit data that contains in class PartyAnimal, kinda like the initial value
    x = 0

    # when the object is construced
    def __init__(self):
        print("I am constructed")

    def party(self):
        self.x += 1
        print("So far",self.x)

    # in here the value of x is destructed and can be RE-USE
    def __del__(self):
        print("I am destructed",self.x)

an = PartyAnimal()
an.party()
an.party()
# we re assign the value of object x
an = 69
print("an contains",an)