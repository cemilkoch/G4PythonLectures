# When a person runs on a treadmill he/she burns 5.6 calories per minute
# Write a program that uses a loop to display the number of calories burned
# after 10, 15, 20, 25, and 30 minutes

for i in range(10, 31, 5):
    print("In {} minutes a person can burn {} calories.".format(i, i * 5.6))

print()
i = 10


while i < 31:
    print("In {} minutes a person can burn {} calories".format(i, i * 5.6))
    i += 5


