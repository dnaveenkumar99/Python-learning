S=set()
for i in range(5):
    data=int(input("Enter a val"))
    S.add(data)
print(S)
S.update([60,70])
print(S)
S.discard(60)
print(S)
