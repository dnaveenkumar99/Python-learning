a=20
def Outer():
    #a=15
    def inner():
        #a=25
        print(a)
    inner()
Outer()