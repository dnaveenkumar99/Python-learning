import random

num=random.randint(1,100)
while True:
    try:
        guess=int(input("Guess the number between 1 and 100:"))
        if guess>num:
            print("Too High!")

        elif guess<num:
            print("Too low!")
        else:
            print("Congratulations! you guessed the number")
            break
    except ValueError:
        print("Please enter a valid number")
