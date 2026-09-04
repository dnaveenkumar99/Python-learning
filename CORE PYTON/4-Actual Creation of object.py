class Hero:
    def __init__(self):
        self.name = "Vijay"
        self.job  = "CM"
        self.numOfMovies = 69
    def act(self):
        print("Vijay is acting")
h1=Hero()
print(h1.name)
print(h1.job)
print(h1.numOfMovies)
h1.act()