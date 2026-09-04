class Human:
    def __init__(self,num_heart):
        self.num_eyes=2
        self.num_nose=1
        self.num_heart=num_heart
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")
class Male(Human):
    def __init__(self,name,heart):
#After defining the init function for the base class
#we need to use the "seper().__init" for accessing the variables of
#parent class
        super().__init__(heart)
        self.name=name
    def flirt(self):
        print("I can flirt")
    #overrinding
    def work(self):
       #Super function will give the access to the methods of parent class
        super().work()
        print("I can code")
    def display(self):
        print(f"Hi, I am {self.name} and I have {self.num_heart} heart.")

male_1=Male("Naveen",1)
male_1.eat()
male_1.work()
male_1.flirt()
print(male_1.num_eyes)
print(male_1.num_heart)