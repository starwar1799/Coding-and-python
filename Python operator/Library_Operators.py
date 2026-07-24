print("Library Visit Planner")
print("Answer 3 Quick questions and I will plan your library visit\n")

day = input("What day is it? (Monday to Sunday): ").strip().capitalize()
weather = input("What is the weather? (sunny/rainy/cloudy): ").strip().lower()
book_due = input("Do you have a book to return (yes/no): ").strip().lower()

if day in ("Saturday", "Sunday"):
    print("Day Type: Weekend- a good time for relaxed library visits")
elif day == "Monday":
    print("Day type: Start of the week check if you have reading list")
elif day == "Friday":
    print("Day type: Last school day for the week return books")
elif day in ("Tuesday", "Wednesday", "Thursday"):
    print("Day Type: Regular school day. Plan a short library Visit")
else:
    print("Day not recognized please type a valid day")

if weather == "sunny" and book_due == "yes":
    print("We have great weather and you can go to the library")

if weather == "rainy" or weather == "cloudy":
    print("Weathe tip: Carry a umbrella if you plab to go to the library")

if not (book_due == "yes"):
    print("No book to return today, browse new books")

if weather == "rainy" and book_due == "yes":
    print("You should use an umbrella and walk carefully and return your book")
elif weather == "sunny" and book_due == "yes" and not (day in("saturday", "Sunday")):
    print("Just go and return and maybe check out a book today")
elif day in ("Saturday", "Sunday") and weather == "sunny":
    print("Today is a really good day for you to go and chill at the library")
else:
    print("Just have a simple library visit")

print()
print("Library plan complete! Happy reading!")