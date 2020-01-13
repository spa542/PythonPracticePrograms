# Basic Conditional Logic
is_old = True;
is_licence = True;

if is_old: 
    print('You are old enough to drive')
    print('This is just a test')
elif is_licence:
    print('You are tuff')
else:
    print('checkcheck')
    
print('WOAHWOAHWOAH')

if is_old is True:
    print('This is a test')

if is_old and is_licence:
    print('You can drive! Congrats!')

# Truthy and Falsey
# when using a variable in a conditional statement, the python interpreter
# will automatically convert the variable into a boolean value
# Good for passwords as an example! You can use truthy and falsey values
# and the boolean will be converted for you, the program will check to see if
# the values are input into

# Ternary Operator
is_old = False if is_licence else 'You are so damn old'
print(is_old)

# Short Circuiting
# Same as always, you can evaluate something before it you move to both or 
# more statements like if the first of the or statements is true then it will
# short circuit and continue to the statements because only one of them needs 
# to be true

# Logical operators!
# They are the same as always
