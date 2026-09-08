import random

while True:
    choice=input("Roll the dice? (yes/no):").lower()
    if choice =="yes":

        d1=random.randint(1,6)
        d2=random.randint(1,6)
        print(f'({d1},{d2})')
    elif choice=="no":
        print("Thank you for playing")
        break
    else:
        print("Invalid choice!")
