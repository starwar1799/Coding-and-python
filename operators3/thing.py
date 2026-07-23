char =  input("Enter a single chracter: ")

if type(char) is str and len(char) ==1:

    print("Valid input!")

else:

    print("Please enter ONE character")

ascii_val = ord(char)

print(f"Character: {char}")

print(f"ASCII Value: {ascii_val}")



