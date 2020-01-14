# Decorator Examples

def hello(func):
    print('helloooooooooooo')

def greetings():
    print('still here!')

# Greet is still pointing to hello function in memory
# When hello is deleted, the actual function is not deleted in memory

a = hello(greetings)

print(hello(greetings))

# Higher Order Function HOC
def greet(func):
    func()

def greet2():
    def func():
        return 5
    return func
