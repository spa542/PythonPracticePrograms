import sys

def main():
    name = 'Ryan'
    # python3 way
    greeting = f'Hello, {name}'
    # python2 way
    greeting2 = 'Hello, {}'
    template = greeting2.format(name)

    print(greeting)
    print(template)

if __name__ == '__main__':
    main()
