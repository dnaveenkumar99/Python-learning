#Normal method
L=[1,2,3,4]
L1=[]
for i in L:
    if i%2 ==0:
        L1.append(i)
print(L1)

#Using list comprehension
L=[1,2,3,4]
L1=[i for i in L if i%2==0]
print(L1)