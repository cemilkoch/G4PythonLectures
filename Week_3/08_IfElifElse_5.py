# Challenge !
# Ask the user for quantity
# suppose that one item will cost 100
# The store will give a discount of 10% if the cost of purchased is more than 1000.
# Calculate the total cost

quantity = int(input("Please enter quantity: "))

cost = quantity * 100

if cost > 1000:
    print("The total cost with 10% discount is", cost * 0.9)
else:
    print("Total cost", cost)
