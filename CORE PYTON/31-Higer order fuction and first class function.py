def fun():
    print("Inside fun1")
def fun2(ptr):
    print("Inside fun2")
    ptr()
    print("leaving fun2")
fun()
fun2(fun)