person = "Sammy"

if person == "Sammy":
    print("Welcome Sammy")
else:
    print("Who are you?")

person_2 = "Jimmy"

if person_2 == "Sammy":
    print("Welcome Sammy")
elif person_2 == "Jimmy":
    print("Welcome Jimmy")
else:
    print("What is your name?")

# -------- Nested if Statements --------

person_3 = 'Peter'
last_name = 'Jackson'
if person_3 == 'Michael':
    if last_name == 'Johnson':
        print("Welcome Michael Johnson")
    else:
        print("Michael, What is your last name?")
elif person_3 == 'Sammy':
    if last_name == 'Jackson':
        print("Welcome Sammy Jackson")
    else:
        print("Sammy, what is your last name?")
else:
    print("Who are you?")

# Challenge !
# Create an x variable store a number you like
# Check if x is positive or not
# if x is positive, check whether x is odd or even number
x = int(input("Please enter a number: "))

if x > 0:
    print("x is positive")
    if x % 2 == 0:
        print("x is even")
    else:
        print("x is odd")
else:
    print("x is negative")

