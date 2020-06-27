# The strip() method removes any whitespace from the beginning or the end:
name = "   Cemil Koc   "
print(name.strip())
print(len(name))

# replace() method replaces a string with another string
a = "Hello Python"
print(a.replace("Python", "Java"))

# The split() method splits the strings into substrings if it finds object we enter
text = "Python Language"
print(text.split(" "))

# Challenge | Split the email address by the @ symbol
prof_address = "michael@nyu.edu"
print(prof_address.split("@"))

# Challenge | Replace the dots(.) with slash(/)
birthday = "09.14.1995"
print(birthday.replace(".", "/"))
print(birthday)