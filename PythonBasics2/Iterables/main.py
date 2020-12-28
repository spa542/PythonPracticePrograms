# Iterables
# An object or collection that can be iterated over
# Can be:
# list, dictionary, tuple, set, string
# iterated -> one by one check each item in the collection

users = { 'name': 'Golem', 'age': 5006, 'can_swim': False }
for item in users:
    print(item)

for item in users.items():
    print(item)

for item in users.values():
    print(item)

for item in users.keys():
    print(item)

for key, value in users.items():
    print(key, value)

my_list = [1,2,3,4,5,6,7,8,9,10]
counter = 0

for item in my_list:
    counter = counter + item
print(counter)
