class Calci:
    def __init__(self):
        self.brand="CASIO"
        self.color="Black"
    def add(self):
        a=10
        b=20
        c=a+b
        return c
c1=Calci()
print(c1.brand)
print(c1.color)
res=c1.add()
print(res)