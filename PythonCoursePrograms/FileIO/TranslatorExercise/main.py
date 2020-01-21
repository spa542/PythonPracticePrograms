# Translator Exercise

try:
    with open('./test.txt', mode='r') as my_file:
        print(my_file.read())
except FileNotFoundError as e:
    print('Check your file path silly!')
