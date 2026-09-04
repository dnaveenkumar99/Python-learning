# class A:
#     def __init__(self):
#         self.a=10
# class B(A):
#     def __init__(self):
#         A.__init__(self)
#         self.b = 20
# class C(B):
#     def __init__(self):
#         B.__init__(self)
#         self.c=30
# c1=C()
# print(c1.c)
# print(c1.b)
# print(c1.a)

#Invoking parent class constructor defaultly
# class A:
#     def __init__(self):
#         self.a=10
# class B(A):
#     def __init__(self):
#         super().__init__()
#         self.b = 20
# class C(B):
#     def __init__(self):
#         super().__init__()
#         self.c=30
# c1=C()
# print(c1.c)
# print(c1.b)
# print(c1.a)

#Different types of inheretience

# single-level-inheritence
# class A:
#     def disp_A(self):
#         print("Inside A")
# class B(A):
#     def disp_B(self):
#          print("Inside B")
# b1=B()
# b1.disp_B()
# b1.disp_A()

#multi level
class A:
    def disp_A(self):
        print("Inside A")
class B(A):
    def disp_B(self):
        print("Inside B")
class C(A):
    def disp_C(self):
        print("Inside c")
B1=B()
C1=C()
B1.disp_B()
B1.disp_A()
C1.disp_C()
C1.disp_A()