# Decorator Exercises

user1 = { 'name': 'Sorna', 'valid': True}

def authenticated(fn):
    def wrapper(dictionary):
        if (dictionary['valid'] == True):
            return fn(dictionary)
        else:
            print('Authentication Failed: Not a valid user')
    return wrapper

@authenticated
def message_friends(user):
    print('Message has been sent')

message_friends(user1)
