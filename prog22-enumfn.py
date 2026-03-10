marks=[12, 45,98,1,49,68]

# index=0
# for mark in marks:
#     print(mark)       #This is too cumbersome and not efficient. We can use the enumerate function to get both the index and the value of each element in the list at the same time, which is more efficient and easier to read.
#     if (index==3):
#         print("index is 3")
#     index = index + 1

for index, mark in enumerate(marks):
    print(mark)      
    if (index==3):
        print("index is 3")
    index = index + 1   
print("\n")
for index, mark in enumerate(marks,
start=1):
    print(mark)
    if(index == 3):
        print("Harry, awesome!" )
        print("\n")
# The enumerate function is a built-in function in Python that allows
# you to loop over a sequence (such as a list, tuple, or string) and get
# the index and value of each element in the sequence at the same
# time. Here's a basic example of how it works:

# Loop over a list and print the index and value of
# each element
fruits = ['apple', 'banana', 'mango' ]
for index, fruit in enumerate(fruits):
    print(index, fruit)
# As you can see, the enumerate function returns a tuple containing the
# index and value of each element in the sequence. You can use the for
# loop to unpack these tuples and assign them to variables, as shown
# in the example above.
print("\n")
for v in enumerate(fruits):
    print(v)