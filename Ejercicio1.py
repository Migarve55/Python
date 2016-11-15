day=int(raw_input("Day: "))
vacations = raw_input("Are you on vacations?: ")

if vacations == "No":
    if (day > 0 and day < 5):
        print("7:00")
    elif (day > 5 and day < 7):
        print("10:00")
elif vacations == "Yes":
    if (day > 0 and day < 5):
        print("10:00")
    elif (day > 5 and day < 7):
        print("off")
