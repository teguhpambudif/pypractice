class PartyAnimal:
    x = 0
    name = ""
    def __init__(self,z):
        self.name = z
        print(self.name,"constructed")

    def party(self):
        self.x += 1
        print(self.name,"party count",self.x)

s = PartyAnimal("Sally")
s.party()

j = PartyAnimal("Jim")
j.party()
# after we make instance of jim, the the object s have different memory address
# so we have 2 independent instance
s.party()