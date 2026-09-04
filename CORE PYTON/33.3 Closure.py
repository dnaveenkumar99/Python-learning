def fun1():
    print("Inside fun1")
    def fun2():
        print("Inside fun2")
    return fun2
res=fun1()
res()


