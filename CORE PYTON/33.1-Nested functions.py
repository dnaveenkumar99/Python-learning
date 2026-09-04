def Outer():
    a=10
    b=20
    print(a)
    print(b)
    def inner():
        nonlocal a #modifies the Outer function variable "a" to 150
        a=150
        nonlocal b
        b=250
        print(a)
        print(b)
    print(a)
    inner()
    print(a)
    print(b)
Outer()