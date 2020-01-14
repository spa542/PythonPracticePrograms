# Creating Decorators
# - Supercharge functions

# Higher Order Function
def my_decorator(func):
    def wrap_func(greeting): # Add func parameters here
        print('***********')
        func(greeting)
        print('***********')
        print('This is the wrapper!')
    return wrap_func

@my_decorator
def hello(greeting):
    print(greeting)

@my_decorator
def bye():
    print('see ya later')

hello('WOah whats up?')
