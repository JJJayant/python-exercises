marks = [3, 5, 6, "Harry", True]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[-1])
print(marks[3])
print(marks[4])

if 6 in marks:
    print("6 is present in the list")

print(marks[2:4]) # Slicing a list

lst=[i**2 for i in range(1,11) if i%2==0] # List comprehension to create a list of squares of even numbers from 1 to 10
print(lst) 

lst.append(12) # Adding an element to the end of the list
print(lst)

lst.sort() # Sorting the list in ascending order
print("The sorted list" ,lst)

lst.sort(reverse=True) # Sorting the list in descending order
print(lst)

lst.reverse() # Reversing the order of the list
print(lst)

print("The index of 16 in the list is:", lst.index(16)) # Finding the index of an element in the list
print("The count of 16 in the list is:", lst.count(16)) # Counting the number of occurrences of an element in the list

#Now we will see how to copy one list to another
m=lst
m[0]=100
print("The original list is:", lst) # This will change the original list as well because m is just a reference to the original list

#The original list is referenced by m and lst, so any change made to m will also affect lst. To create a copy of the list, we can use the copy() method or the list() constructor.
n=lst.copy() # This will create a copy of the list
n.insert(1,117) # This will not affect the original list. It will insert 117 at index 1 in the copied list n. The original list lst will remain unchanged. 
print("The original list is:", lst)
print("The copied list is:", n) 
lst.extend(n) # This will extend the original lst by adding all the elements of the copied list n to it. The original list lst will now contain all the elements of both lists. The copied list n will remain unchanged.
print(lst) 
o=lst+n # This will concatenate the original list lst and the copied list n and create a new list o. The original list lst and the copied list n will remain unchanged.
print(o)