# Error Handling Stuff

while True:
    try:
        age = int(input('What is your age? '))
        print(age)
    except ValueError:
        print('Please enter a valid number')
    except ZeroDivisionError:
        print('Please enter an age greater than 0')
    else:
        print('Thank you very much!')
        break
    finally:
        print('Ok, I am finally done')
