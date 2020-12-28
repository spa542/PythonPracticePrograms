# Formatted Strings
name = 'Johnny'
age = 55

print('hi ' + name + '. You are ' + str(age) + ' years old')

# Add f in front within the print function **Python3 only!
print(f'hi {name}. You are {age} years old')

# Add .format() and your argumenmts **Python2 or lower
print('hi {0}. You are {1} years old'.format(name, age))
# or
print('hi {}. You are {} years old'.format(name, age))
