def adder(x, y, z):
    print("Sum:", x + y + z)


adder(10, 12, 13)


# *args (Non Keyword Arguments)
# Create a function that sums the numbers that are entered as parameters
def adder_2(*args):
    sum_num = 0

    for i in args:
        sum_num += i

    print("Sum:", sum_num)


adder_2(3, 5)
adder_2(3, 4, 5, 6, 7, 8)


# Keyword Arguments
# **kwargs (KEYWORD ARGUMENTS)
# key=value


def information(**kwargs):
    print("Data type of argument", type(kwargs))
    for k, v in kwargs.items():
        print(k, v)


information(Firstname="Cemil", Lastname="Koc", Age=25, Phone=2147569809)


def km_to_mph(kilometers):
    return kilometers * 0.6214


print(km_to_mph(20))

