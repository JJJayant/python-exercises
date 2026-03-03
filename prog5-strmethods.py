# Strings are immutable
a="!!Jayant!! dsfk!!"
b="introduction tO Python"
print(a.upper())
print(a.lower())
print(a.rstrip('!')) #This will remove the trailing exclamation marks
print(a.lstrip('!')) #This will remove the leading exclamation marks 
print(a.strip('!')) #This will remove both leading and trailing exclamation marks
print(a.replace('Jayant', 'Nikita')) #This will replace all occurrences of 'a' with 'o'
print(a)
print(a.split(' ')) #This will split the string into a list of substrings based on the space character
print(a.find('dsfk')) #This will return the index of the first occurrence of 'dsfk' in the string
print(a.count('!')) #This will count the number of occurrences of '!' in the string 

print(b.capitalize()) #This will capitalize the first letter of the string
print(b.title()) #This will capitalize the first letter of each word in the string
print(b.center(30)) #This will center the string in a field of width 30
print(len(b.center(30)))
print(a.endswith('!!')) #This will return True if the string ends with '!!' and False otherwise
print(a.startswith('!!')) #This will return True if the string starts with '!!'
print(b.find('Python')) #This will return the index of the first occurrence of 'Python' in the string
print(b.find('python')) #This will return -1 as 'python' is not found
print(a.isalnum()) #This will return False as the string contains special characters
print(a.isspace()) #This will return False as the string contains non-space characters
print(a.isalpha()) #This will return False as the string contains special characters and spaces

print(a.isupper()) #This will return False as the string contains lowercase letters
print(a.istitle()) #This will return False as the string is not in title case
print(a.swapcase()) #This will swap the case of each letter in the string