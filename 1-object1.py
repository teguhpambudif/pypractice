class PartyAnimal:
    x = 0

    def party(self):
        self.x += 1
        print("So far", self.x)

# asigning partyanimal class into an object
an = PartyAnimal()

an.party()
an.party()
an.party()

print("Type:", type(an))
print("Dir:",dir(an))