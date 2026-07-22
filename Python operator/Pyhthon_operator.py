print("Smart School Day Planner")
print("Answer 3 questions for day planning /n")

day = input("What day is it (sunday to saturday): ").strip().capitalize()
weather = input("What's the weather like (sunny or rainy): ").strip().lower()
homework = input("You do your work? (yes/no): ").strip().lower()

print()
print(f" ypur plan for {day}")
print("." * 35)

if day in ("Saturday", "Sunday"):
    print("Day type     : Weekend - enjoy your free time")
elif day == "Monday":
    print("Day Type         First Day Of School Week Pack your stuff.")
elif day == "Friday":
    print("Day Type         Last school day for the week :D return school books")
elif day in ("Tuseday", "Wednesday", "Thursday"):
    print("Day type         Normal boring day")
else:
    print("Day type: none. You probably spelled it wrong")

if weather == "sunny" and homework == "yes":
    print("After school you can go to the park cause you did your work and its nice weather today")

if weather == "rainy" or weather == "cloudy":
    print("you should pprobably get an umbrella because if its windy enough you can start flying")

if not (homework == "yes"):
    print("You didnt do yur homework. Do it now")

if weather == "rainy" and not (homework == "yes"):
    print("Just do your homework please and stay inside")

elif weather == "sunny" and homework == "yes" and not (day in("saturday, sunday")):
    print("you did everything but its a school day so you  wont have the tme to go outside")

elif day in ("Saturday", "Sunday") and weather == "sunny":
    print("You literally have the best weekend outcome go outside")
else:
    print("i dont know at this point just good luck")

print()
print("have a good day")