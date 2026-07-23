print("Enter a number (numerator): ")
numn = int(input())
print("Enter a number (denominator): ")
numd = int(input())

if numn%numd==0:
    print("\n" +str(numn)+ "is divisibe by" + str(numd))
else:
    print("\n" +str(numn)+ "is not divisibe by" + str(numd))