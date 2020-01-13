# Global Keyword

total = 0

def count():
    global total
    total += 1
    return total

# Puts total into the global context
# - Better to use paramters instead of global keyword

# nonlocal keyword

def outer():
    x = 'local'
    def inner():
        nonlocal x
        x = 'nonlocal'

