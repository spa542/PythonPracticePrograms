# Docstrings
def text(a):
    '''
    Info: This function tests and prints param a
    '''
    print(a)

# In a regular IDE the docstring will appear when cursor is in the brackets
# You can also use help(functionName) to print out the docstring
# Use functionName.__doc__ and print that to print the docstring to console
# help(text)
print(text.__doc__)
text(a)

