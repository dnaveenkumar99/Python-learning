class Fan: #class creation
    def __init__(self): #constructor
        self.brand = "Usha" #properties of the object
        self.cost  = 2000
        self.color = "White"
        self.wings = 3
    def ON(self): #Methods/Behaviours
        print("Fan is ON")
    def Rotate(self):
        print("Fan is Rotating")
    def OFF(self):
        print("Fan is OFF")
f1 = Fan() #Creating Object
print(f1.brand) #Accessing the variables
print(f1.cost)
print(f1.color)
print(f1.wings)

f1.ON() #calling the methods
f1.Rotate()
f1.OFF()
