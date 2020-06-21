# Rules for Variable Names
# Variable names can't start with a number
# Variable names can't contain spaces, instead we can use underscores snake_case
# Variable names can't contain symbol : '<>!$@

my_cats = 4
print(my_cats)

my_cats = 6
print(my_cats)

b = 10

# Reassigning Variables

b = b + b + b
print(b)

c = 20
c = c + 10
print(c)
# There is a shortcut for writing the code above
# +=
c += 10  # c = c + 10
print(c)

a = 4
a *= 2
print(a)

y = 25
y /= 5
print(y)

# Dynamic Typing

name = "John"
print(type(name))

name = 25.5
print(name)
print(type(name))

