class Demo:
    def __init__(self):
        self.a=10
    def __disp(self):
        print("Inside disp")
    def helper(self):
        self.__disp()
d1=Demo()
d1.helper()