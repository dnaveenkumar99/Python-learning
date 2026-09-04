
class Plane:
    def takeoff(self):
        print("Fligth is taking off")
    def fly(self):
        print("Fligth is flying")
class Pp(Plane):
    def carry(self):
        print("pp is carrying p")
class Cp(Plane):
    def carry(self):
        print("Cp is carrying g")
class Fp(Plane):
    def carry(self):
        print("Fp is carrying W")
p=Pp()
c=Cp()
f=Fp()
def allowplane(ref):
    ref.takeoff()
    ref.fly()
    ref.carry()
allowplane(p)
allowplane(c)
allowplane(f)


#Method overloading
# class A:
#     def disp(self,a,b,c):
#         print(a)
#         print(b)
#         print(c)
# class B(A):
#     def disp(self,a,b):
#         print(a)
#         print(b)
# class C(B):
#     def disp(self,a):
#         print(a)
#
# c1=C()
# c1.disp(10)
# c1.disp(10,20)
# c1.disp(10,20,30)

#How to overcome method overriding
# class A:
#     def disp(self):
#         print("A")
# class B:
#     def disp(self):
#         print("B")
# class C:
#     def disp(self):
#         print("C")
#         B.disp(self)
#         A.disp(self)
# c1=C()
# c1.disp()