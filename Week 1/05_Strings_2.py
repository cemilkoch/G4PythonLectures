parrot = "Norwegian Blue"

# index() method is used to retrieve the index number of a character in a string
print(parrot.index("n"))

# len() method is used to get the length of a string
print(len(parrot))

# Finding negative index of a character
print(parrot.index("w") - len(parrot))
print(parrot[-11])
print()
# Challenge : print
# w
# e
#
# w
# i
# n
# using the letters from the variable parrot
print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])
print("********************\n")

# Challenge : Print the numbers only
title = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H, 9:I"
print(title[::5])
print(title[0::5])
print(title.index("1") - len(title))
print(title[-43::5])

print()
# Challenge : Print the letters only
print(title[2::5])
print(title[-41::5])
