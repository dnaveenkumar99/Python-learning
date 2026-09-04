#NO PARAMETER NO RETURN VALUE
def add():
    a=2
    b=3
    c=a+b
    print(c)
add()

#NO PARAMETER WITH RETURN VALUE
def add():
    a=8
    b=9
    c=a+b
    return(c)
res=add()
print(res)

#WITH PARAMETER  NO RETURN VALUE
def add(x,y):
    c=x+y
    print(c)
add(2,5)

#WITH PARAMETER WITH RETURN VALUE
def add(x,y):
    c=x+y
    return(c)
res=add(5,6)
print(res)