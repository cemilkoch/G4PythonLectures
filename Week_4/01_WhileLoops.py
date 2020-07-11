# While Loops

x = 0

# while Condition:
#     do some action

while x < 10:
    print("X is currently :", x)
    print("X is still less than 10, adding 1 to X")
    x += 1
    if x == 5:
        print("X is now 5")
        break
    else:
        print("Continue...")
        continue
else:
    print("Loop has finished iterating!")

# Write a program to add numbers up to user_input | sum = 1 + 2 + 3 + 4...... user_input

number = int(input("Enter a number: "))
i = 1
add = 0

while i <= number:
    add += i  # add = add + i
    i += 1

print("The addition is :", add)
