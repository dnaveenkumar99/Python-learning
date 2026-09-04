class Heroine:
    def __init__(self):
        self.name="Anuhska"
        self.age=43
    def dance(self):
        print("Anuska is a good dancer")
h1=Heroine()
print(h1.name)
print(h1.age)
h1.dance()
h1.movie="Billa"
print(h1.movie)
h1.age=44
print(h1.age)
del h1.movie
print(h1.movie)
