str=input("Enter a string")
print(str)
if str.isalpha():
    print("Contains only alphabets")
elif str.isdigit():
    print("Contains only numbers")
elif str.isalnum():
    print("Contains both")
else:
    print("Some other character")