# Debugging in Python

# linting 
# ide / editor
# read errors
# print debugging
# pdb
import pdb

def add(num1, num2):
    pdb.set_trace()
    return num1 + num2

add(3, 'asdfas')
