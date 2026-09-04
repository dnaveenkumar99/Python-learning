L=[]
i=0
while True:
    n1=int(input("Enter a number:"))
    L.insert(i,n1)
    i=i+1
    print("Do you want to continue?")
    print("Press 1.YES 2.NO")
    choice=int(input())
    if choice==1:
        continue
    else:
        break
print(L)



# L=[]
# i=0
# while True:
#
#     n1=int(input("Enter a number:"))
#     L.insert(i,n1)
#     i=i+1
#     print("Do you want to continue:")
#     print("Press 1.YES 2.NO")
#     choice=(int(input()))
#     if choice==1:
#         continue
#     elif choice==2:
#         break
#     else:
#         print("Invalid selection")
# print(L)

