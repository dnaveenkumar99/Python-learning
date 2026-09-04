def Outer():
    print("Inside outer")
    def inner():
        print("Inside inner")
    inner()
Outer()
