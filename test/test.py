print("Calculator")
num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))
math_type = str(input("What math type do you want to use (Options are ADDITION, SUBTRACTION, MULTIPLICATION, DIVISION)(Enter in all caps fully or it won't be taken) : "))
if math_type == "ADDITION":
    def ADDITION (num1,num2):
        AddAnswer = num1 + num2
        print(f"{num1} + {num2} = {AddAnswer}")
elif math_type == "SUBTRACTION":
    def SUBTRACTION (num1,num2):
        SubAnswer = num1 - num2
        print(f"{num1} - {num2} = {SubAnswer}")
elif math_type == "MULTIPLICATION":
    def MULTIPLICATION (num1,num2):
        MultAnswer = num1 * num2
        print(f"{num1} * {num2} = {MultAnswer}")
elif math_type == "DIVISION":
    def DIVISION (num1,num2):
        DivAnswer = num1 / num2
        print(f"{num1} / {num2} = {DivAnswer}")
elif math_type == "DIVISION" and num1 or num2 == 0:
    ZeroDivisionError
    print("I know what you are trying to do. No.")
else:
    print("No. We either don't have that (sorry) or you cant read directions. Restart this you dont get anymore.")

print("Ok you done. goodbye :D")
