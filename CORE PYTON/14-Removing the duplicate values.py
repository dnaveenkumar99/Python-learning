str=input("Enter a string:")
str1=""
for i in str:
    if i not in str1:
        str1=str1+i
    else:
        pass
print(str1)

#if i in str1:
   # pass
#else:
    #str1=str1+i