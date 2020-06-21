# To Create a String in Python we can use '' or ""

print(type("Silicone Labs"))
print('Hello')

name = "Cemil"
print(name)

text = "I'm a programmer"  # \' to create a single quote or use double quotes or use triple quotes
print(text)

text_1 = "Use \nto print a new line"  # \n creates a new line
print(text_1)

# Slicing
# 0123456...
s = "Hello World"
# variable[start:end]

print(s[0])  # H
print(s[6])  # W

# Retrieve Hello
print(s[:5])
print(s[0:5])

# World
print(s[6:])
print(s[6:11])

# Step point
# variable[start:end:step point]
print(s[0:11:3])
print(s[::3]) # HlWl beginning to end with 3 steps
print("stepping point of 2", s[:5:2])

# Retrieve W r
print(s[6:9:2])
print("*****************\n")

# In python ending characters start from negative -1
  #      -4 -3 -2 -1
str_1 = "Java"  # a = -1 = 3
                # v = -2 = 2

print(str_1[-1])
print(str_1[-2])
print(str_1[2])

# Reversing a string
print(str_1[::-1])

a = 35
b = 45.9
c = "Cemil"

# print(b + c)

