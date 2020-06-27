# Accessing Tuple Elements
# Use [] to access an item in tuples

my_tuple = ('p', 'y', 't', 'h', 'o', 'n')
print(my_tuple[0])
print(my_tuple[-1])

# print(my_tuple[6]) index out of range

# Nested Tuples
n_tuple = ('Mouse', (1, 2, 3, 4))
print(n_tuple[1][1])

# Changing a tuple element
# Tuples are immutable

my_tuple_2 = (4, 2, 3, [6, 5])
# my_tuple_2[1] = 5
my_tuple_2[3][0] = 20
my_tuple_2[3].append(7)
print(my_tuple_2)

# Reassignment
my_tuple_2 = ('S', 'Q', 'L')
print(my_tuple_2)

# del my_tuple_2[1]

# We can delete the entire tuple
del my_tuple_2
# print(my_tuple_2)

my_tuple_3 = ('a', 'p', 'p', 'l', 'e')
print(my_tuple_3.count('p'))
print(my_tuple_3.index("l"))

my_tuple_4 = ('b', 'a', 'n', 'a', 'n', 'a')

# in keyword
print('b' in my_tuple_4)
print('t' in my_tuple_4)

# not in keyword
print('g' not in my_tuple_4)
