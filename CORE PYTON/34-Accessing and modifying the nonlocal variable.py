def Outer():
    a=10
    b=20
    print(a)
    print(b)
    def inner():
        nonlocal a
        a=150
        b=250
        print(a)
        print(b)
    print(a)
    inner()
    print(a)
Outer()