#Value Errors
# input:10 , five
# try:
#     a=int(input("Enter a num:"))
#     b=int(input("Enter a num:"))
#     res=a/b
#     print(res)
# except ValueError as e:
#     print ("It is a VE")
# except ZeroDivisionError as e:
#     print("It is a ZDE")
# except Exception as e:
#     print("Other Error")

#Other errors
# try:
#     a=int(input("Enter a num:"))
#     b=input("Enter a num:")
#     res=a/b
#     print(res)
# except ValueError as e:
#     print ("It is a VE")
# except ZeroDivisionError as e:
#     print("It is a ZDE")
# except Exception as e:
#     print("Other Error")

# #Single block for multiple exceptions
# try:
#     a = int(input("Enter a num:"))
#     b = int(input("Enter a num:"))
#     res = a / b
#     print(res)
# except( ValueError,ZeroDivisionError) as e:
#     print("It is a VE or ZE")
#
# except Exception as e:
#     print("Other Error")

try:
     a = int(input("Enter a num:"))
     b = int(input("Enter a num:"))
     res = a / b
     print(res)
except Exception as e:
    print("error occured")
    # print(e.__str__())
    #or
    print(e)