# Python docstrings are the string literals that appear
# right after the definition of a function, method, class,
# or module.

def square(n):
    '''This function takes a number as input and returns its square.
    The function uses the exponentiation operator to calculate the square of the number.'''
    print(n**2)

square(2.3)
print(square.__doc__, "\n") # This will print the docstring of the function square. The __doc__ attribute of a function contains its docstring.

# PEP-8 is a style guide for Python code that provides guidelines and best practices on how to write Python code. 
# It covers various aspects of code formatting, such as indentation, line length, naming conventions, and more. Following PEP-8 can help improve the readability and maintainability of your code.
import this # This will print the Zen of Python, which is a collection of aphorisms that capture the philosophy of Python. The Zen of Python was written by Tim Peters and is included as an Easter egg in the Python interpreter. It provides insights into the design principles and philosophy of Python programming language.