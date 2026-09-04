from math import pi
#pi=20
def Outer():
    #pi=15
    def inner():
        #pi=25
        print(pi)
    inner()
Outer()