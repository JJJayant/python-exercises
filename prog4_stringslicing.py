name= "Jayant Jain"
print(" My name is of length", len(name))
print(name[0:6])
print(name[:6])#The first index is by default 0
print(name[7:])#The last index is by default the length of the string
print(name[-4:])#Negative indexing starts from the end of the string
print(name[::2])#This is called slicing with step size of 2
print(name[5:1]) #This will print an empty string as the starting index is greater than the ending index