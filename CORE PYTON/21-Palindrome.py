str=input("Enter a string:")
rev=""
for i in str:
    rev=i+rev
if rev==str:
    print("Palondrome")
else:
    print("not")