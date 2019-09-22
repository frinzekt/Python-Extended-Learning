#
# Example file for working with functions
#

# define a basic function


def func1():
    print("Hello?")

# function that takes arguments


def func2(x):
    print(x)


# function that returns a value
# default value
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

# function with default value for an argument

# mutli *args or rest parameter has to be the last parameter


def multi_add(*args):
    result = 0
    for x in args:
        result += x
    return result

# **kwargs is another term
# used for keyworded elements


def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))


print(greet_me(name="abc", age="def"))

# function with variable number of arguments


print(power(2))
print(power(2, 3))
print(power(x=3, num=2))
# python can call arguments that are not in order if named

print(multi_add(1, 2, 3, 4))
print(multi_add(1, 2, 3, 41, 1, 1))
