# The + operator concatenates only Strings.

s = "Apple"
t = "iPhone"
u = "11 Pro"
y = 8
print(s + " " + t)

# Without Whitespace
print(s + t + u)

# With WhiteSpace
print(s + " " + t + " " + u)

print(s, t, y)

# The * operator will print multiple copies of a String
name = "Cemil."
print(name * 6)
print((name + " ") * 5)

# The number may be negative or zero. But it will not print with negative or zeros.
# It will print an empty string
print("name * -8" + name * -8)

str_1 = 'I love programming with'
str_2 = "Python"
print(str_1, str_2)

print()
# STRING METHODS

str_3 = "I am learning Python, Java"
str_4 = "capitalize me"
str_5 = "capitalize all the words please"

# upper() method
print(str_3.upper())

# lower() method
print(str_3.lower())

# capitalize()
print(str_4.capitalize())

# title() method
print(str_5.title())

# split() by a specific element
print(str_3.split())
print(str_3.split(","))


# .format()
print("Insert another string with curly brackets: {}".format("The inserted String"))
print("My name is {} and my last name is {}".format("Cemil", "Koc"))

name = "Adam"
last_name = "Johnson"
print("His name is {} and his last name is {}".format(name, last_name))

# Placeholder method %s Python 2.7
print("I am going to inject %s here" % "something")
print("I am going to inject %s text, and %s text here" % ("some", "more"))

print()
x, y = 'some', 'more'

print("I am going to inject %s text, and %s text here." % (x, y))

# Format conversion methods
# %d it is used for integers
print("I wrote %d programs today" % 4)

# %f it is used for floating number

print("Floating point numbers: %0.6f" % (3.141516))
