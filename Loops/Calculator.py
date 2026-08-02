base = int(input("Enter the base: "))
exponent = int(input("Enter exponent: "))
answer = 1
for i in range(1, exponent+1):
    answer = base * answer
print(answer," is your answer")
    