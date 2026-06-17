class Mobile:
    def __init__(self):
        self.brand="Vivo"
    def display(self):
        print("Mobile is displaying")
    @staticmethod
    def call():
        print("Mobile is calling")
    @classmethod
    def game(cls):
        print("Mobile is gaming")
m1=Mobile()
print(m1.brand)
m1.display()
Mobile.call()
Mobile.game()