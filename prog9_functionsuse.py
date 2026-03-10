def geometric_mean(x, y):
    mean= (x * y) ** 0.5
    print("The geometric mean is:", mean)

def isgreater(g,h):
    pass

a=input("Enter the first number: ")
b=input("Enter the second number: ")
geometric_mean(float(a), float(b))

# There are four types of arguments that we can provide in a function:
# · Default Arguments
# · Keyword Arguments
# . Variable length Arguments
# · Required Arguments

def avg(a=9,b=6):#We can provide a default value while creating a function. This way the function can be called without providing any argument. If we provide an argument, then the default value will be overridden.
    print("the average is:", (a+b)/2)

avg(9) # Here we are providing only one argument, so the default value of b will be used. The average will be calculated as (9+6)/2 = 7.5
avg(b=5) # Here we are providing only one argument, so the default value of a will be used. The average will be calculated as (9+5)/2 = 7.0
avg() # Here we are not providing any argument, so the default values of a and b will be used. The average will be calculated as (9+6)/2 = 7.5
avg(8,4) #If the default arguments are not provided, then the arguments are called required arguments. The average will be calculated as (8+4)/2 = 6.0
avg(b=4,a=10) #Keyword arguments allow us to specify the arguments by their names, so the order of the arguments does not matter. The average will be calculated as (10+4)/2 = 7.0

print("\n")
#Variable length arguments allow us to provide a variable number of arguments to a function. We can use the * operator to indicate that we want to accept a variable number of arguments. The arguments will be passed as a tuple to the function.
def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print("the average is", sum/len(numbers))
    print(type(numbers))
average(2,3,8,90,4)

#Using dictionary as an argument
def name(**name):
    print(type(name))
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname = "James")