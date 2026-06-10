import time
deposit_amount=2000
print("=======WELCOME=======")
#Customer info
Name=input("Enter your Name:")
Mobile_number=int(input("Enter your Mobile number:"))
Adhaar_number=int(input("Enter your Adhaar number:"))
Driving_licence_number=input("Enter your Driving Licence number:")

#Type of vechicles available
print("\nSelect the type of vechicle:")
print("1.Two wheeler\n2.Four Wheeler")
vehicle_req=int(input())
selected_vehicle=""
vehicle_price=0
if vehicle_req==1:
    print("\nselect the two wheeler type:")
    print("1.Bike\n2.Scooter:")
    choice_1=int(input())
    if choice_1==1:
        print("\nAvailable bikes:")
        print("1.Bullet - Rs.1000/day")
        print("2.Pulsar - Rs.750/day")
        print("3.Splendor - Rs.600/day")
        bike_choice=int(input("\nSelect the bike:"))
        if bike_choice==1:
            selected_vehicle="Bullet"
            vehicle_price=1000
        elif bike_choice==2:
            selected_vehicle="Pulsar"
            vehicle_price=750
        elif bike_choice==3:
            selected_vehicle="Splendor"
            vehicle_price=600
        else:
            print("Invalid bike selection")
            exit()
    elif choice_1==2:
        print("\nAvailable scooters:")
        print("1.Ntorq - Rs.700/day")
        print("2.Vespa - Rs.500/day")
        print("3.Activa - Rs.400/day")
        bike_choice=int(input("Select the scooter:"))
        if bike_choice==1:
            selected_vehicle = "Ntorq"
            vehicle_price = 700
        elif bike_choice == 2:
            selected_vehicle = "Vespa"
            vehicle_price = 500
        elif bike_choice == 3:
            selected_vehicle = "Activa"
            vehicle_price = 400
        else:
            print("Invalid scooter selection")
            exit()
elif vehicle_req==2:
    print("\nAvailable cars:")
    print("1)Punch - Rs.1600/day")
    print("2)Swift - Rs.1800/day")
    print("3)Ertiga - Rs.2000/day")
    car=int(input("Select the car:"))
    if car==1:
        selected_vehicle="Punch"
        vehicle_price=1600
    elif car==2:
        selected_vehicle="Swift"
        vehicle_price=1800
    elif car==3:
        selected_vehicle="Ertiga"
        vehicle_price=2000
    else:
        print("Invalid car selection")
else:
    print("Invalid vehicle selection")
    exit()
rental_days=int(input("How many days do you want to rent?\n"))

total_bill=vehicle_price*rental_days+deposit_amount
time.sleep(1)

print("="*40)
print("              Rental bill")
print("="*40)
print("\nCustomer details:-")
print(f"Name:{Name}")
print(f"Mobile number:{Mobile_number}")
print(f"Adhaar number:{Adhaar_number}")
print(f"DL number:{Driving_licence_number}")

print("\nRental details:-")
print(f"Selected vehicle:{selected_vehicle}")
print(f"Selected vehicle rent:{vehicle_price*rental_days}")
print(f"Deposit amount:{deposit_amount}")
print(f"Total amount:{total_bill}")
print("\n            Thankyou")
print("="*40)









