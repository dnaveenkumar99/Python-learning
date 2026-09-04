str=" Pavan is waste "
print(str)
str1=str.lstrip()
print(str1)
str2=str.rstrip()
print(str2)

str3=input("Enter a string")
str4=""
for i in str3:
    if i==" ":
        pass
    else:
        str4=str4+i
print(str4)