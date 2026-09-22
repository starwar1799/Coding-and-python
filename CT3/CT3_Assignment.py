John = {"name": "John", "score": 70}
Jim = {"name": "Jim", "score": 80}
Jeff = {"name": "Jeff", "score": 90}
Jerome = {"name": "Jerome", "score": 100}
Joe = {"name": "Joe", "score": 69}

chosen_student = str(input("Which student are you looking for? (Joe, Jim, Jeff, Jerome, John (Type how it's shown)): "))

if chosen_student == "John":
    print(John)

elif chosen_student == "Jim":
    print(Jim)

elif chosen_student == "Jeff":
    print(Jeff)

elif chosen_student == "Jerome":
    print(Jerome)

elif chosen_student == "Joe":
    print(Joe)

else:
    print("Who is this?")