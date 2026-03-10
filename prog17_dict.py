dic={"Name":"jayant", "Age":22, "City":"Pune"}
# print (dic("Name")) # This will give an error because we are trying to call the dictionary as a function. To access the value of a key in a dictionary, we can use square brackets [] or the get() method.
print(dic["Name"]) # This will print the value of the key "Name" in the dictionary dic. If the key "Name" is not present in the dictionary, it will raise a KeyError. To avoid this, we can use the get() method, which returns None if the key is not present in the dictionary.
print(dic.get("Name")) # This will print the value of the key "Name" in the dictionary dic. If the key "Name" is not present in the dictionary, it will return None.
print(dic.keys()) # This will print a view object that contains the keys of the dictionary dic. The view object is dynamic, which means that if we add or remove keys from the dictionary, the view object will reflect those changes.
print(dic.values()) # This will print a view object that contains the values of the dictionary dic. The view object is dynamic, which means that if we add or remove keys from the dictionary, the view object will reflect those changes.

for i in dic.keys(): # This will iterate over the keys of the dictionary dic and print each key. We can also use the items() method to iterate over the key-value pairs of the dictionary.
    print("The value corresponding to the key", i, "is", dic[i]) # This will print the value of each key in the dictionary dic, separated by a space. The end parameter in the print() function is used to specify the string that is printed at the end of the output. By default, it is a newline character (\n), but we can change it to a space or any other string. In this case, we are using a space to separate the values of the keys in the dictionary.

print(dic.items()) # This will print a view object that contains the key-value pairs of the dictionary dic as tuples. The view object is dynamic, which means that if we add or remove keys from the dictionary, the view object will reflect those changes.
print(dic)

emp1={122:98,128:45,132:83}
emp2={123:78,129:56,133:90} 

emp2.update(emp1) # This will add the key-value pairs from the dictionary emp1 to the dictionary emp2. If there are any duplicate keys, the values from the dictionary emp1 will overwrite the values in the dictionary emp2. The original dictionary emp2 will be modified, but the original dictionary emp1 will remain unchanged.
print(emp2)
emp2.pop(122) # This will remove the key-value pair with the key 122 from the dictionary emp2 and return the value associated with that key. If the key 122 is not present in the dictionary emp2, it will raise a KeyError. To avoid this, we can use the pop() method with a default value, which will return the default value if the key is not present in the dictionary.
print(emp2)
del emp1[128] # This will remove the key-value pair with the key 128 from the dictionary emp1. If the key 128 is not present in the dictionary emp1, it will raise a KeyError. To avoid this, we can use the pop() method, which will return the value associated with the key if it is present, or a default value if it is not present.
emp1.clear() # This will remove all the key-value pairs from the dictionary emp1, making it an empty dictionary. The original dictionary emp1 will be modified, but the original dictionary emp2 will remain unchanged. 
print(emp1)
# del emp1 # This will delete the dictionary emp1 from memory. After this, we cannot access the dictionary emp1 because it has been deleted. If we try to access it, it will raise a NameError.