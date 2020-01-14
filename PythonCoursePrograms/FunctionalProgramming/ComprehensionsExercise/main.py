# Comprehensions Exercise

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

new_list = [ letter for letter in some_list if some_list.count(letter) <= 1]
print(new_list)
