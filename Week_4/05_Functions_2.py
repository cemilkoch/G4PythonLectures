def absolute_value(number):
    # if number >= 0:
    #     return number
    # else:
    #     return -number
    return abs(number)


print(absolute_value(2))
print(absolute_value(-5))


def my_function():
    x = 10
    print("Value inside the function", x)


x = 20
print("Value outside the function", x)
my_function()


# A simple function to check whether x is even or odd
def even_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")


even_odd(4)
even_odd(5)

# To add multiple amount of arguments(parameters) in a function
# We can use *args


def my_function_2(*words):
    for i in words:
        print(i, end=" ")


my_function_2("Hello", "Welcome", "to", "Python", "Class")
