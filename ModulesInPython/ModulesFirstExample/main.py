# Main Module

from utility import multiply, divide
# This can become cumbersome
# import shopping.more_shopping.shopping_cart
# Use this
# from shopping.more_shopping.shopping_cart import buy
# Or import the entire module!
from shopping.more_shopping import shopping_cart

print(multiply(5,4))

print(shopping_cart.buy('bike'))

print(divide(5,2))

print(__name__)

if __name__ == '__main__':
    print('please run this')
