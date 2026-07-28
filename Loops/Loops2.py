string = input("Please enter a string: ")

#firstway
string2 = ('')
#loop for printing in reverse
for i in string:
    string2 = i + string2

print("\nThe Original String =", string)
print("The Reversed String = ", string2)

#OTHER WAY
print("The Reversed String =", string[::-1])