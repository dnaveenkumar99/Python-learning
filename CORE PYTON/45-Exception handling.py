# def fun1():
#     print("Enter fun1:")
#     try:
#         fun2()
#     except Exception as e:
#         print("Error occured in fun1")
#     print("Leaving fun1")
# def fun2():
#     print("Entering fun2")
#     res=10/0
#     print(res)
#     print("Leaving fun2")
# print("Pgm started")
# fun1()
# print("Pgm end")

#Rethrowing an error in excptional handling
# def fun1():
#     print("Entering fun1")
#     try:
#         fun2()
#     except Exception as e:
#         print("Error occured in fun1")
#     print("Leaving fun1")
# def fun2():
#     print("Entering fun2")
#     try:
#         res=10/0
#         print(res)
#     except Exception as e:
#         print("Error occured in fun2")
#         # raise e
#     print("Leaving fun2")
# print("Pgm started")
# fun1()
# print("pgm ended")

# use finally keyword
# def fun1():
#     print("Entering fun1")
#     try:
#         fun2()
#     except Exception as e:
#         print("Error occured in fun1")
#     print("Leaving fun1")
# def fun2():
#     print("Entering fun2")
#     try:
#         res=10/0
#         print(res)
#     except Exception as e:
#         print("Error occured in fun2")
#         raise e
#     finally:
#         print("Leaving fu2")
#     print("Leaving fun2")
# print("Pgm started")
# fun1()
# print("pgm ended")


#Using Else block
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
try:
    res=a/b
    print(res)
except Exception as e:
    print("Error occured")
else:
    print("Program ran succesfully")