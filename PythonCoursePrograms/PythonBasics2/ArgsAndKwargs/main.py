# *args and **kwargs
# *args allows any amount of arguments to be passed
# **kwargs allows you to add any amount of keywords as arguments
def super_func(*args, **kwargs):
    print(args)
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super_func(1,2,3,4,5, num1=5, num2=10))

# Rule: actual paramters, *args, default parameters, **kwargs
