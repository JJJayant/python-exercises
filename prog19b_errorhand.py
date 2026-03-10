#HANDLING ERROR
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
    #print("I am always executed")
    #Even though the function returns a value in the except block, the finally block will still be executed before the function returns.
    #This is because the finally block is designed to execute regardless of whether an exception was raised or not, and it will always run before the function exits. Therefore, in this case, the output will include the message "I am always executed" followed by the return value of 0 if an IndexError occurs, or 1 if the input index is valid.
x = func1()
print(x)

#RAISING CUSTOM EXCEPTIONS
a=int(input("Enter a number betwen 1 and 10: "))
if(int(a)<1 or int(a)>10):
    raise ValueError("Invalid input! Please enter a number between 1 and 10.") # This will raise a ValueError with the specified error message if the user input is not within the valid range. The raise statement is used to explicitly trigger an exception when a certain condition is met, allowing us to handle it appropriately in our code. In this case, if the user enters a number less than 1 or greater than 10, the program will raise a ValueError and display the error message to inform the user about the invalid input.
else:
    print("You entered a valid number: ", a)