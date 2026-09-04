class Human:
    def __init__(self,num_heart):
        print("Calling init from Human")
        self.num_eyes=2
        self.num_nose=1
        self.num_heart=num_heart

    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")
class Male:
    def __init__(self,name):
        print("Calling init from Male")
        self.name=name
    def flirt(self):
        print("I csn flirt")
    def work(self):
        print("I can code")
class Boy(Human,Male):
    def __init__(self,name,heart,language):
        Human.__init__(self,heart)
        Male.__init__(self,name)
        self.language=language
    def sleep(self):
        print("I can sleep")
    def work(self):
        print("I can test")


boy_1=Boy("Rahul",1,"python")
print(boy_1.num_nose)
print(boy_1.num_heart)
print(boy_1.language)

print(Boy.mro())
#We can't access the work method of male class because
#it is the second argument of the boy class
#so we need to use the below method to call the work method of the
#male class
#Male.work(boy_1)