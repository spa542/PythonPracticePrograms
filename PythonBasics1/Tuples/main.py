# Tuple
# Like lists but they are immutable
my_tuple = (1,2,3,4,5)

print(my_tuple)
print(5 in my_tuple)

# When using dictionary.items() it will return our key and values as multiple
# tuples. This is important because it shows that they are immutable

user = { (1,2): [1,2,3], 'greet': 'hello', 'age':20 }

print(user[(1,2)])

new_tuple = my_tuple[1:2]

print(new_tuple)

x,y,z, *other = (1,2,3,4,5)
print(other)
