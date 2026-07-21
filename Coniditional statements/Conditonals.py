temperature = int(input("Enter The Temperature Of Today In Celsius"))

if temperature < 20:
    outfit = "jacket"
    print("It is cold today")
    print("Wear a", outfit)
else:
    outfit = "shirt"
    print("It is warm today")
    print("Wear a", outfit)

is_raining = input("It it raining? (Do not use spaces) (yes/no):")
if is_raining == "yes":
    print("bring an umbrella")

wind_speed = int(input("Enter the wind speed in km/h: "))

if wind_speed > 30:
    needs_jacket = "yes"
    print("It is windy today")
    print("where a jacket with your", outfit)
else:
    needs_jacket = "no"
    print("It's not windy  today")
    print("You don't need a jacket today")

has_puddles = input("Are there puddles on the ground? (yes or no)")

if has_puddles == "yes":
    shoes = "boots"
    print("The ground is wet")
    print("wear", shoes)
else:
    shoes = "running shoes"
    print("The ground is dry")
    print("wear", shoes)

print("You did all the weatheer checking.")

print("Today's outfit")
print("Temperature:", temperature)
print("Outfit Chosen:", outfit)
print("Raining:", is_raining)
print("Jacket Needed:", needs_jacket)
print("Shoes Needed:", shoes)