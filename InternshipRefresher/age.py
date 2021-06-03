import sys

def main():
    user_age = input('Enter your age: ')

    years = int(user_age)

    months = years * 12

    print(f'Your age is equal to {months} months')

if __name__ == '__main__':
    main()
