# Generator Examples
# range() is a generator
# iterable - an object that we can loop through
# has dunder method __iter__
# Generators are iterable

range(100)
list(range(100))

def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result

my_list = make_list(100)
print(my_list)

# Defining our own generator
# yield - function that pauses and comes back to the function when next() is 
# called
# ***If it has yield it is a generator
def generator_function(num):
    for i in range(num):
        yield i

g = generator_function(100)
next(g)
next(g)
print(next(g))


