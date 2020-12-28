# Lists - an ordered sequence of objects that can be any type
li = [1,2,3,4,5]
li2 = ['a','b','c']
li3 = [1,2,'a',True]

print(li[0])

# Data Structure
# Square brackets allow us to put multiple related items but unrelated data types
# together in one list 
# Lists are not immutable!!!!
li2[1] = 'not a character'

# List Slicing
print('List Slicing')
print(li3[0::2])

# String Slicing
print('String Slicing')
string = 'hellloooo'
print(string[0:2:1])

# List Methods
basket = [1,2,3,4,5]
print(len(basket))
# *list methods use a . after the list
basket.append(100)
new_list = basket
new_list.append(5000)
print(new_list)
new_list.extend([500, 1, 2, 4])
print(new_list)
# removing like a stack
basket.pop()
basket.pop()
basket.pop(2)
basket.remove(4)
print(basket)
basket.clear()
print(basket)

# Other functions
l4 = [1,2,3,4,5,6,7,8,9]
print(l4.index(2))
print(l4.index(5, 0, 8))
# Can use 'in' keyword
print(2 in l4)
print(l4.count(5))
l5 = [1,5,4,3,6,7,8]
print('Current list ')
print(l5)
l5.sort()
print('Sorted list ')
print(l5)

# List unpacking
print('List unpacking')
a,b,c, *other = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(other)
