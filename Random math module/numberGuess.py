import random
playing = True
number = str(random.randint(0,20))

print("I will generate a number 0-20. Go guess")
print("Ths game ends when you guess the exact number")
while playing:
    guess = input("Give me guess \n")
    if number == guess:
        print ("You win. \n")
        print(f"the number was, {number}. \n")
        break

    else:
        print("Your guess isnt right. \n")