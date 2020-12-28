# Pure Functions
# 1. Same input = Same output ALWAYS!
# 2. Function should not produce any side effects

from functools import reduce

my_list = [1,2,3]
your_list = [10,20,30]
def multiply_by2(item):
    return item*2

def check_odd(item):
    return item % 2 != 0

def accumulator(acc, item):
    print(acc, item)
    return acc + item
    
# Special Functions: map, filter, zip, and reduce

# map()
print(list(map(multiply_by2, my_list)))
print(my_list)

# filter()
print(list(filter(check_odd, my_list)))
print(my_list)

# zip()
print(list(zip(my_list, your_list)))
print(my_list)
print(your_list)

# reduce()
print(reduce(accumulator, my_list, 0))
print(my_list)
