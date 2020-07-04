# We use {} to create a dictionary
# An item has a key and a corresponding value
# that is expressed as a pair {key:value}
# Dictionaries are mutable
# Dictionaries are unordered

# Empty Dictionary
my_dictionary = {}
print(type(my_dictionary))
print(my_dictionary)

# Dictionary with integers
my_dictionary_2 = {1: 'apple', 2: 'banana', 3: 'orange'}
print(my_dictionary_2)

personal_details = {'name': 'Cemil', 'last_name': 'Koc', 'age': 25}
print(personal_details)

# Dictionary with mixed DataTypes
my_dictionary_3 = {'name': 'John', 3: [1, 2, 3, 4]}

# Creating dictionary using dict()
my_dictionary_4 = dict({1: 'apple', 2: 'pear'})

# Retrieving elements from the dictionary
# get() and [] to retrieve your elements
my_dictionary_5 = {'name': 'Jack', 'age': 27}
print(my_dictionary_5['name'])
print(my_dictionary_5.get('age'))

# Changing and Adding Elements to a dictionary
my_dictionary_5['age'] = 28
print(my_dictionary_5)
my_dictionary_5.update({'age': 29})

# Adding element
my_dictionary_5['address'] = "Montclair"
print(my_dictionary_5)

# Removing an element from the Dictionary
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# pop() function
squares.pop(4)
print(squares)

# popitem() function
squares.popitem()
print(squares)

# clear()
squares.clear()
print(squares)
