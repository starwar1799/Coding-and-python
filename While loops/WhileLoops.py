total_choores = 4
original_count = total_choores
print(f"You have {original_count} chores to finish today!\n")

completed_count = 0
chore_num = 1

while chore_num <= total_choores:
    if chore_num == 1: next_chore = "feed your bed"
    elif chore_num == 2: next_chore = "take out the the pet"
    elif chore_num == 3: next_chore = "make the trash"
    else: next_chore = "fight the laundry"

    answer = input(f"Have you finished: {next_chore}? (yes/no): ")

    if answer == "yes":
        completed_count += 1
        chore_num += 1
        print("Great job! chore completed.")
    else:
        print("Okay finish it and check again!")

    print("Chores remaining:", total_choores - completed_count)

print("==== All chores complete! ====")
print("Great work doing all the work")