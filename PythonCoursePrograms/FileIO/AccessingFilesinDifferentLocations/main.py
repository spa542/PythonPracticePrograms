# Accessing Files in Different Locations

try:
    with open('/home/ryan/Desktop/sad.txt', mode='r') as my_file:
        print(my_file.read())
except FileNotFoundError as err:
    print('File does not exist / not found')
except IOError as err:
    print('IO error here')
