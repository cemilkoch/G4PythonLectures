name = input("Enter a name: ")

if name == "Max":
    print("Name entered is: ", name)
elif name == "Eli":
    print("Name entered is: ", name)
else:
    print("The name entered is invalid!")

# Challenge
# Ask the user for a time(24 hr)
# if the time is before 10 say "Good morning"
# if the time is after 10 and before 12 say "soon time for a lunch"
# if the time is after 12 and before 18 say "have a good day"
# if the time is after 18 and before 22 say "Good Evening"
# if the time is after 22 say "Good night"

time = int(input("Enter a time: "))
if 0 <= time < 24:
    if time <= 10:
        print("Good Morning")
    elif 10 < time <= 12:
        print("Soon time for a lunch")
    elif 12 < time <= 18:
        print("Have a good day")
    elif 18 < time <= 22:
        print("Good Evening")
    else:
        print("Good night")
else:
    print("Invalid time")

