L = [4, 5, 1, 2, 9, 7, 10, 8]
print("Original List:", L)

count = 0

for i in L:
    count += i

avg = count/len(L)

print("sum =", count)
print("Average =", avg)

L.sort

print(L)

print("Smallest element:", L[0])

print("Largest element:", L[-1])