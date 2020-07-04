# Range function
# Range function is a built-in function that returns a sequence

list_1 = list(range(0, 10))  # range(10)

print(list_1)

list_2 = list(range(0, 11, 2))
print(list_2)


for i in list_1:
    print(i)
print()

# Even numbers in list_1
for i in list_1:
    if i % 2 == 0:
        print(i)
    else:
        print("Odd number")

# Challenge
# Print them in same line
# print them in reverse order

list_3 = list(range(15))

for i in list_3[::-1]:
    print(i, end=" ")

print()

for i in range(15, 0, -2):
    print(i, end=" ")

