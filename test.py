import utility #how to import module
import shopping.shopping_cart  #how to import packages
from shopping.more_shopping.deeper_buy import buy

print(utility.new_multiply(2, 3))
print(shopping.shopping_cart.buy('apple'))
print(buy("orange"))




# if __name__ == '__main__':      This line says "if this file is the one being run do something

print(__name__)