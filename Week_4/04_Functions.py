# How to create a function
# def == defining a function

def name_of_function():
    print("Hello")


name_of_function()
name_of_function()


def say_hello():
    '''
    DOCSTRING: Information about the function
    INPUT: no input
    OUTPUT: hello how are you?
    :return:
    '''
    print("Hello How are you?")


say_hello()


# parameterized function

def greeting(name="Sammy"):
    print("Hello", name)


greeting("Jimmy")
greeting()


# Function to add 2 numbers
def add_nums(num_1, num_2):
    """
    This function adds two numbers
    :param num_1:
    :param num_2:
    :return:
    """
    return num_1 + num_2


print(add_nums.__doc__)
add = add_nums(15, 20)
print(add_nums(15, 30))
print(add)


# Create a function to check if a number is prime or not
# Prime number is a number that can be divided to 1 and the number itself
# E.g 2, 3, 5, 7, 11, ....

def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            print(number, "is not prime!")
            break
        else:
            print(number, "is prime")
            break


is_prime(11)
is_prime(4)
is_prime(14)

