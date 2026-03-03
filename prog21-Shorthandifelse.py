a=210
b=30
print("A") if a>b else print("=") if a==b else print("B") # This is a shorthand if-else statement, also known as a ternary operator. It allows us to write a simple if-else statement in a single line of code. In this case, it checks if a is greater than b, if they are equal, or if b is greater than a, and prints the corresponding output accordingly.

c=9 if a>b else 0
print (c) # This is another example of a shorthand if-else statement. It assigns the value 9 to c if a is greater than b, otherwise it assigns 0 to c. In this case, since a is greater than b, c will be assigned the value 9 and that will be printed as the output.

#This is not readible and should be avoided for complex conditions.
#   It is better to use a regular if-else statement for better readability and maintainability of the code.