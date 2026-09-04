#Shallow copy
# L=[10,20,30,40]
# print(L)
# L1=L #Shallow coopy
# print(L)
# print(L1)
# L[1]=200
# print(L)
# print(L1)

#Deep copy
# L=[100,200,300,400]
# print(L)
# L1=L.copy() #Deep copy
# print(L)
# print(L1)
# L[1]=800
# print(L)
# print(L1)



#Deep copy will not work for nested list
# L=[100,200,["shiva","sus"],30]
# print(L)
# L1=L.copy()
# print(L)
# print(L1)
# L[1][0]="wife"
# print(L)
# print(L1)


#Achieving deep copy in a nested list
import copy
L=[100,["shiva","sus"],30]
print(L)
L1=copy.deepcopy(L)
print(L)
print(L1)
L[1][1]="wife"
print(L)
print(L1)
