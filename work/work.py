secret_number = 51
print("Guess my secret number it's a number from 1- 100  no decimals or fractions)")
guess_1 = int(input("Print your first guess: "))
guess = 1
if guess_1 == 51:
    print("the number was 51 good job")
    set win = True
elif guess_1 == range(1, 10+1) or range(90, 100+1):
    print("ICE COLD GUESS")
elif guess_1 == range(11, 20+1) or range(80, 89+1):
    print("Cold guess")
elif guess_1 == range(21, 40+1) or range(60, 79+1):
    print("Hot guess! Almost there")
elif guess_1 == range(41, 59+1):
    print("SUPER HOT GUESS!!!!!!!!!  SO CLOSE JUST A BIT MORE!!!")

guess = 2
guess_2 = int(input("Print your second guess: "))
if guess_2 == 51:
    print("the number was 51 good job")
    set win = True
elif guess_2 == range(1, 10+1) or range(90, 100+1):
    print("ICE COLD GUESS")
elif guess_2 == range(11, 20+1) or range(80, 89+1):
    print("Cold guess")
elif guess_2 == range(21, 40+1) or range(60, 79+1):
    print("Hot guess! Almost there")
elif guess_2 == range(41, 59+1):
    print("SUPER HOT GUESS!!!!!!!!!  SO CLOSE JUST A BIT MORE!!!")

guess = 3
guess_3 = int(input("Print your third guess: "))
if guess_3 == 51:
    print("the number was 51 good job")
    set win = True
elif guess_3 == range(1, 10+1) or range(90, 100+1):
    print("ICE COLD GUESS")
elif guess_3 == range(11, 20+1) or range(80, 89+1):
    print("Cold guess")
elif guess_3 == range(21, 40+1) or range(60, 79+1):
    print("Hot guess! Almost there")
elif guess_3 == range(41, 59+1):
    print("SUPER HOT GUESS!!!!!!!!!  SO CLOSE JUST A BIT MORE!!!")

guess = 4
guess_4 = int(input("Print your fourth guess: "))
if guess_4 == 51:
    print("the number was 51 good job")
    set win = True
elif guess_4 == range(1, 10+1) or range(90, 100+1):
    print("ICE COLD GUESS")
elif guess_4 == range(11, 20+1) or range(80, 89+1):
    print("Cold guess")
elif guess_4 == range(21, 40+1) or range(60, 79+1):
    print("Hot guess! Almost there")
elif guess_4 == range(41, 59+1):
    print("SUPER HOT GUESS!!!!!!!!!  SO CLOSE JUST A BIT MORE!!!")

guess = 5
guess_5 = int(input("Print your final guess: "))
if guess_5 == 51:
    print("the number was 51 good job")
    set win = True
elif guess_5 == range(1, 10+1) or range(90, 100+1):
    print("ICE COLD GUESS")
elif guess_5 == range(11, 20+1) or range(80, 89+1):
    print("Cold guess")
elif guess_5 == range(21, 40+1) or range(60, 79+1):
    print("Hot guess! Almost there")
elif guess_5 == range(41, 59+1):
    print("SUPER HOT GUESS!!!!!!!!!  SO CLOSE JUST A BIT MORE!!!")

if guess >= 6 and <=50:
    print("You were not able to guess the number in time. the number waas 12")
    if win = true set guess to 53
if guess =  53:
    print("you won.")
