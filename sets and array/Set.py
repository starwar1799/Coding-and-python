basket1 = {"Mango", "triangle", "Tangerine", "Strawberry", "Lemon"}
basket2 = {"Orange", "Strawberry", "Lime"}
print("Basket 1:", basket1)
print("Basket 2:", basket2)

basket1.add("Pineapple")
print("basket 1 after adding pineapple:", basket1)

common_fruits = basket1.intersection(basket2)
print("Fruits in both baskets:", common_fruits)

import array as arr
fruits_counts = arr.array('i', [6, 7, 3, 13])
print("Fruits counts array:", fruits_counts)

fruits_counts.insert(3, 11)
fruits_counts.append(6)
print("Fruits counts after adding items:", fruits_counts)

count_of_4 = fruits_counts.count(4)
print("Number of timews 4 appears", count_of_4)

fruits_counts.reverse()
print("reversed fruits counts array:", fruits_counts)

print("")
print("FRUIT BASKETS ORGANIZED")
print("BASKET1: ", basket1)
print("BASKET2: ", basket2)
print("Shared fruits: ", common_fruits)
print("Fruit counts: ", fruits_counts)
