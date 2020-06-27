# List Methods

# Creating a list
list_1 = []
print(list_1)

# Addition of Elements into the list_1 append()
list_1.append(10)
list_1.append(3.14)
list_1.append(25)

print("List after adding elements", list_1)

# insert() method
box = ["TV"]
box.insert(1, "Bicycle")
box.insert(2, "Lamp")
print(box)

box.insert(0, "macBook")
print(box)

# extend() method
list_2 = [1, 2, 3, 4]
list_2.extend([5, 6, 7])
print(list_2)

# Updating Elements in list
box_2 = ["Fish", "Cat", "Dog"]
box_2[1] = "Bird"
print(box_2)

# Deleting elements
del box_2[2]
print("My dog died", box_2)

print()
# remove(), pop(), clear()
ch_list = ['A', 'B', 'F', 'H', 'O']
ch_list.remove('B')
print(ch_list)

# pop() if you don't enter an index number, it will remove the last element
ch_list.pop(2)
print(ch_list)

# clear()
ch_list.clear()
print(ch_list)

# Challenge !
list_3 = [20, 25, ["Ford", "BMW", "Toyota", "Honda"], [2016, 2017]]
# Please remove FORD
# Please insert 2018 and 2019 in the nested list
list_3[2].remove("Ford")
list_3[3].extend([2018, 2019])
print(list_3)
