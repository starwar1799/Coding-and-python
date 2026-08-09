print("Square Pattern Of Stars (*):")
row = int(input("Enter the number of rows:"))
for i in range(0,row,1):
    print(end="* ")
    for j in range(1,row,1):
        print(end="* ")
    print()
