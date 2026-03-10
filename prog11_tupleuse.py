tup=(1,3, "green") #tuples are imutable sequences, which means that once we create a tuple, we cannot change its elements. We can create a tuple by enclosing the elements in parentheses () and separating them with commas. We can also create a tuple without using parentheses, by just separating the elements with commas. However, it is recommended to use parentheses for better readability.
print(type(tup),tup)

if 3 in tup:
    print("3 is present in the tuple")
    tup2=tup[2:3] # Slicing a tuple
    print(tup2)

tup4=(24,3,68,2,79)
lst=list(tup4) # We can convert a tuple to a list using the list() constructor. This will create a new list with the same elements as the tuple. The original tuple will remain unchanged.
lst.append("Hello") # We can add an element to the list using the append() method. This will add the element to the end of the list. The original tuple will remain unchanged.
lst.pop(2) # We can remove an element from the list using the pop() method. This will remove the element at the specified index and return it. The original tuple will remain unchanged.
tup4=tuple(lst) # We can convert the list back to a tuple using the tuple() constructor. This will create a new tuple with the same elements as the list. The original list will remain unchanged.
print(lst)
tup5=tup+tup4 # We can concatenate two tuples using the + operator. This will create a new tuple that contains all the elements of both tuples. The original tuples will remain unchanged.
print(len(tup5), tup5) # We can find the length of a tuple using the len() function. This will return the number of elements in the tuple. We can also print the tuple to see its elements.
print(tup5.count(3)) # We can count the number of occurrences of an element in a tuple using the count() method. This will return the number of times the specified element appears in the tuple.
print(tup5.index(3)) # We can find the index of the first occurrence of an element in a tuple using the index() method. This will return the index of the first occurrence of the specified element in the tuple. If the element is not found, it will raise a ValueError.
print(tup5.index(3, 4)) # We can also specify a starting index for the search using the second argument of the index() method. This will return the index of the first occurrence of the specified element in the tuple starting from the specified index. If the element is not found, it will raise a ValueError.
print(tup5.index(3, 4, 6)) # We can also specify a starting and ending index for the search using the third argument of the index() method. This will return the index of the first occurrence of the specified element in the tuple starting from the specified starting index and ending at the specified ending index. If the element is not found, it will raise a ValueError.