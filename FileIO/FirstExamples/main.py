# File I/O First Examples

my_file = open('test.txt', mode='r+')

print(my_file.read())
my_file.seek(0)
print(my_file.read())
my_file.seek(0)

print(my_file.readline())

my_file.seek(0)
print(my_file.readlines())

text = my_file.write('Hey it\'s me')
print(text)

my_file.close()

with open('sad.txt', mode='w') as new_file:
    text = new_file.write(':(')
    print(text)



# Actually want to do it with this...
# This is so you don't have to close the file on your own
# with open('test.txt') as my_file:
#    print(my_file.readlines())
