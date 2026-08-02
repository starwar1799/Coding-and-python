print("Welcome to holiday planner")

print("step 1: pick you holiday type")
print(" 1- beach holiday")
print(" 2- mountain holiday")
print()

choice = int(input("enter 1 or 2: "))
print()

if choice == 1:
    print("Step 2: pick your beach activity")
    print(" 1- Swimming")
    print(" 2-building a sandcastle")

    beach_activity = int(input("Enter 1 or 2: "))
    print()

    if beach_activity == 1:
        print("You picked swimming. Morning is the best time for this remember to bring water and sunscreen")

    if beach_activity == 2:
        print("You picked sandcastle building. the best time to do this is evening you need a bucket and shovel")
    else:
        print("This is not an eligible option. pick 1 or 2")

elif choice == 2:
    print("Step 2: pick your mountain activity")
    print(" 1- Hiking")
    print(" 2- camping")

    mountain_activity = int(input("Enter 1 or 2: "))
    print()

    if mountain_activity == 1:
        print("You picked hiking. this is best if you feel like exporing trails and remember to wear comfortable shoes and bring water and other supplies.")

    if mountain_activity == 2:
            print("You picked camping. this is bet when you want to stay close to nature. Carry a tent, flashlight and other camping essentials")

else:
     print("that is not valid")
     print("Pick 1 or 2")


print("Goodbye!")
print("Enjoy your vacation")


