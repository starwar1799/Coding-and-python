n0 = int(input("Just enter 1 number. for rainy write a 0 for sunny write anything above 0 that isnt a decimal: "))
n1 = int(input("Just enter another number. for rainy write a 0 for sunny write anything above 0 that isnt a decimal: "))
n2 = int(input("Just enter another number. for rainy write a 0 for sunny write anything above 0 that isnt a decimal: "))
n3 = int(input("Just enter another number. for rainy write a 0 for sunny write anything above 0 that isnt a decimal: "))
n4 = int(input("Just enter another number. for rainy write a 0 for sunny write anything above 0 that isnt a decimal: "))
n5 = int(input("Just enter another number. for rainy write a 0 for sunny write anything above 0 that isnt a decimal: "))
n6 = int(input("Just enter another number. for rainy write a 0 for sunny write anything above 0 that isnt a decimal: "))
n7 = int(input("Just enter another number. for rainy write a 0 for sunny write anything above 0 that isnt a decimal: "))
n8 = int(input("Just enter another number. for rainy write a 0 for sunny write anything above 0 that isnt a decimal: "))
n9 = int(input("Just enter another number. for rainy write a 0 for sunny write anything above 0 that isnt a decimal: "))
n10 = int(input("Just enter another number. for rainy write a 0 for sunny write anything above 0 that isnt a decimal: "))
weather=(n0,n1,n2,n3,n5,n6,n7,n8,n9,n10)
sunny=0
rainy=0
for i in range(0,10):
    if(weather[i]==0):
        rainy+=1
    else:
        sunny+=1

if(sunny>rainy):
    print("Sunny weather")
elif range(0,5) == sunny:
    print("equal chances")
else:
    print("It's gonna rainNnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn")