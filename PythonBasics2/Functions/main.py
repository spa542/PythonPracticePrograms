# Functions
def say_hello():
    print('Hello')

say_hello()

# Parameters
# Positional arguments -> position matters
def say_hello(name, emoji):
    print('Hello ' + name + ' ' + emoji)

# Arguments
say_hello('Ryan', '*')

# Keyword arguments
say_hello(emoji= '*', name = 'Bibi')

# Default Parameters
def say_hello(name = 'Darth Vader', emoji = '*_*', birth = '11/29'):
    print('Hello LOL you thought!')

# Return Types, none need to be specified, just needs the 'return' keyword
def sumOfTwo(num1, num2):
    return num1 + num2

print(sumOfTwo(1,2))
