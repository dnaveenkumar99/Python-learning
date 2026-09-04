class Auto:
    def __init__(self):
        self.brand="Bajaj"
        self.colour="Yellow"
    def carry(self):
        print("Auto carries passangers")
        self.cost=700000
        print("self.cost")
        print(self)
a1=Auto()
print(a1.brand)
print(a1.colour)
#print(a1.cost)
a1.carry()
print(a1.cost)
print(a1)