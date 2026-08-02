print("Welcome to Ride Builder!")

print("Step 1: Pick Your Vehicle")
print(" 1-Bike")
print(" 2-car")

choice = int(input("Enter 1 or 2: "))
print()

if choice ==1:
    print("step 2: Pick a bike")
    print(" 1- Scooty")
    print(" 2- Mountain bike")
    print()

    bike_type = int(input("Enter 1 or 2: "))
    print()

    if bike_type == 1:
        print("You picked: Scooty")
        print("Top Speed: 100 km/h")
        print("Best for: Anything and everything")

    else:
        print("You picked: Mountain Bike")
        print("Top Speed: 20 km/h")
        print("Best for: Off road trails")

elif choice == 2:
    print("Step 2: Pick your car type")
    print("1- Sedan")
    print("2- SUV")
    print()

    car_type = int(input("Enter 1 or 2: "))

    if car_type == 1:
        print("You picked: Sedan")
        print("Seats: 5 passangers")
        print("Best for: Family Trips")
    else:
        print("You picked: SUV")
        print("Seats: 7 passangers")
        print("Best for: off road trips")
else:
    print("That's not valid.")
    print("Pick 1 or 2")

print()
print("Your ride is ready!")
print("Enjoy Your journey!")