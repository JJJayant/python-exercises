a=input("Enter the number whose multiplication table you want:")
print(f"The multiplication table of {a} is:")

#The user can also give a string as an input, which will cause an error when we try to perform multiplication. 
# To handle this error, we can use a try-except block to catch the exception and print an error message instead of crashing the program.

# for i in range (1,11):
#     print(f"{a} x {i}= ", int(a)*i)

try:
    for i in range (1,11):
        print(f"{a} x {i}= ", int(a)*i) 

except Exception as e:
    print("Invalid input! Please enter a valid number. The error message is:", e)

print("\n lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut ")

#We can also handle specific types of errors, such as ValueError, which occurs when we try to convert a non-numeric string to an integer.
b=input("Enter a number: ")
try:
    c=[2,4,3,5]
    print(c[int(b)]) # This will try to access the element at the index specified by the user input. If the user input is not a valid integer or if it is out of range for the list, it will raise an exception.
except ValueError:
    print("Invalid input! Please enter a valid number. The error message is: ValueError: invalid literal for int() with base 10: '{}'".format(a))    
except IndexError:
    print("IndexError: list index out of range") #Multiple except blocks can be used to handle different types of exceptions separately, allowing for more specific error handling and messaging. In this case, we are catching both ValueError and IndexError, which are common exceptions that can occur when working with user input and list indexing, respectively. By providing specific error messages for each type of exception, we can help the user understand what went wrong and how to fix it. 


def func1():
    try:
        l = [1, 5, 6, 7]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    except IndexError:
        print("Index out of bounds!")
        return 0
    finally:
        print("I am always executed")
    # print("I am always executed")

x = func1()
print(x)