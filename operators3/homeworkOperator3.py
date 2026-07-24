char =  input("Enter a single chracter: ")

if type(char) is str and len(char) ==1:

    print("Valid input!")

else:

    print("Please enter ONE character")

ascii_val = ord(char)

print(f"Character: {char}")

print(f"ASCII Value: {ascii_val}")


print("\nCharacter Type: ", end="")
if ascii_val >= 65 and ascii_val <=90:
    print("Uppercase Letter")
elif ascii_val >= 97 and ascii_val <= 122:
    print("Lowercase Letter")
elif ascii_val >= 48 and ascii_val <= 57:
    print("Digit")
elif ascii_val == 32:
    print("Space") 
else:
    print("Special Character")

