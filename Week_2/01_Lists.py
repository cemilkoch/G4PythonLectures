# List may contain DataTypes like integers, Strings, floats, booleans...

# Creating a list
list_1 = []
print("Empty List", list_1)

# Creating a list of numbers
list_2 = [10, 15, 20, 25]
print("List of numbers", list_2)

# Creating a list of strings
programming_languages = ["Java", "C++", "Python", "JavaScript", "SQL"]

# Accessing the elements of the list
print("Index number 1", programming_languages[1])
print("Index number 2", programming_languages[2])

# Create a multi-dimensional list(Nested Lists)
shopping_list = [["Apples", "Oranges", "Bananas"], ["Cheese", "Milk", "Eggs"]]
print("\nShopping List", shopping_list)
print(shopping_list[0][2])

# Lists can have duplicate values
list_3 = [1, 2, 3, 3, 3, 4, 4, 5, 5]
print(list_3)

# Lists can have mixed type of values (Having numbers and strings)
list_4 = [1, 4, ["Address", "Gorilla", "Lion"], 3.14, True]
print(list_4)
print(len(list_4))
