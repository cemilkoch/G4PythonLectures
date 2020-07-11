import random

# Write a program to ask if user wants to roll the dice(1,6)
# If the user say yes, then roll the dice and print it.
# Ask the user if they want to roll the dice again
# Keep asking until user says no

question = input("Would you like to roll the dice? (Y/N) ").lower()

while question == "yes" or question == "y":
    i = random.randint(1, 6)
    print(i)
    question = input("Would you like to roll again? ").lower()
    # if question == "n" or question == "no":
    #     break
