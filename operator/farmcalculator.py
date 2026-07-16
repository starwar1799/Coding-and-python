field1 = 120
field2 = 180
field3 = 240
field4 = 300
field5 = 360

total = field1 + field2 + field3 +field4 +field5
average = total / 5

print("total harvest:", total, "kg")
print("Average per field :", average, "kg")

price_per_kg = 15
earnings = total * price_per_kg
print("total earnings : Rs.", earnings)

bags = total//25
leftover = total % 25

print("full bags packed  :", bags)
print("leftover grain  :", leftover, "kg")

last_year = 500
print("Better than last year? :", total > last_year)
print("same as last year? :", total == last_year)
print("at least like last year? :", total >= last_year)

total += 30
print("After bonus crop :", total, "kg")

total -= 15
print("After reserving seeds :", total, "kg")

bags = total // 25
print("After bags packed :", bags, "bags")