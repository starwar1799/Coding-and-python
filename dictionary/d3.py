country_code = {'India' : '0001','South Korea' : '0002','Japan' : '0003',}

print("Countery code for India -")
print(country_code.get('India', 'not found'))

print("Countery code for China -")
print(country_code.get('china', 'not found'))