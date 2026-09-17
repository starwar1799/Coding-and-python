items = ["pencil", "eraser", "notebook", "sharpener", "glue"]
stock_counts = [12, 0, 8, 5, 3]

inventory = {item: count for item, count in zip(items, stock_counts)}
print("Full Inventory:", inventory)

in_stock_items = [item for item in items if inventory[item] > 0]
print("Item In Stock:", in_stock_items)

chosen_item = input("WHich item will you buy?: ")
if chosen_item not in inventory:
    print("nuh uh. we don't have ", chosen_item, " go somewhere else")
    exit()
elif inventory[chosen_item] == 0:
    print("we dont have ", chosen_item, "Our bad. give us a bit to restock.")
    exit()

prices = [93.99, 75.50, 69.99, 55.00, 99.99]
markup = int(input("Enter the markup amount which is for ALL ITEMS: "))

marked_up_prices = list(map(lambda p: p + markup, prices))
print("Marked Up Prices: ", marked_up_prices)

item_index = items.index(chosen_item)
chosen_price = marked_up_prices[item_index]
print("Price of ", chosen_item, "after markup: ", chosen_price)

inventory[chosen_item] = inventory[chosen_item] -1
print(chosen_item, "purchased. we got ", inventory[chosen_item])

print("")
print("SSIC")
print("You got: ", chosen_item)
print("You paid: ", chosen_price)
print("We got: ", inventory, "left")
print("byeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")