import sys

def main():
    name = input('Enter you name: ')

    print(name)

    # input always gives a string
    temp = input('Enter meters: ')

    square_meters = float(temp)**2

    print(f'Square meters is {square_meters}')


if __name__ == '__main__':
    main()
