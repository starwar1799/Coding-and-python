class Parrot:


    species = "bird"

    def __init__(self, name, age):
        self.age = age
        self.name = name

Blu = Parrot("Blu", 10)
Wu = Parrot("Wu", 15)
Ru = Parrot("Ru", 0.5)

print("Blu is a {}".format(Blu.species))
print("Wu is also a {}".format(Wu.species))
print("Ru is another {}".format(Ru.species))

print("{} is {} years old".format( Blu.name, Blu.age))
print("{} is {} years old".format( Wu.name, Wu.age))
print("{} is {} years old".format( Ru.name, Ru.age))
