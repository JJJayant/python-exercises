# a set is a collection of unique elements. It is unordered and mutable. It is defined using curly braces {} or the set() constructor. 
# A set can contain elements of different data types, but it cannot contain duplicate elements.
#  Sets are useful for performing mathematical operations like union, intersection, difference, and symmetric difference.

s={1,56,23,2,23,56,"jayant", "JAYANT"} # This will create a set with unique elements. The duplicate elements will be removed.
print(type(s), s)

t={}
print(type(t), t) # This will create an empty dictionary, not an empty set. To create an empty set, we can use the set() constructor.
s2={2,56,77,17}

s3=set() # This will create an empty set.
# s3=set(4,64,"hello", "world") # This will give an error because the set() constructor takes only one argument, which is an iterable. We can pass a list or a tuple to the set() constructor to create a set.
print(type(s3), s3)

s3=s2.union(s) # This will create a new set that contains all the unique elements from both sets s1 and s. The original sets s1 and s will remain unchanged.
print(type(s3), s3)
print(s2.intersection(s)) # This will create a new set that contains only the elements that are present in both sets s1 and s. The original sets s1 and s will remain unchanged.
print(s2.difference(s)) # This will create a new set that contains only the elements that are present in set s1 but not in set s. The original sets s1 and s will remain unchanged.
print(s2.symmetric_difference(s)) # This will create a new set that contains only the elements that are present in either set s1 or set s but not in both sets. The original sets s1 and s will remain unchanged.
s.update(s2) # This will add all the unique elements from set s2 to set s. The original set s will be modified, but the original set s2 will remain unchanged.
print(type(s), s)
print(s.isdisjoint(s2)) # This will return False because there are common elements between sets s and s2. If there were no common elements, it would return True.
print(s.issubset(s3)) # This will return True because all the elements of set s are present in set s3. If there were any element in set s that is not present in set s3, it would return False.
print(s.issuperset(s2)) # This will return True because all the elements of set s2 are present in set s. If there were any element in set s2 that is not present in set s, it would return False.
s.add(170) # This will add the element 170 to set s. If the element 170 is already present in set s, it will not be added again because sets do not allow duplicate elements.
print(type(s), s)
s.remove(170) # This will remove the element 170 from set s. If the element 170 is not present in set s, it will raise a KeyError. To avoid this, we can use the discard() method, which does not raise an error if the element is not present in the set.
s.discard(170) # This will remove the element 170 from set s if it is present. If the element 170 is not present in set s, it will do nothing and will not raise an error.
print(type(s), s)
del s3 # This will delete the set s3 from memory. After this, we cannot access the set s3 because it has been deleted. If we try to access it, it will raise a NameError.
s2.clear() # This will remove all the elements from set s2, making it an empty set. The original set s2 will be modified, but the original set s will remain unchanged.
print(type(s2), s2)