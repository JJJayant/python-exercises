# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end now append three random characters at the starting and the end 
# else: simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it else: remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode
import random
import string

choix=input("Welcome to Spylang! Do you want to code or decode? (Enter 'code' or 'decode')")
if choix=="code":
    a=input("Enter your message to be encoded: ")
    if len(a)>=3:
        b=a[1:]+a[0]
        c1=letters = string.ascii_letters
        c="".join(random.choices(c1,k=3))+b+"".join(random.choices(c1,k=3))
    else:
        c=a[::-1]
    print("Your encoded message is: ", c)
elif choix=="decode":
    a=input("Enter your message to be decoded: ")
    if len(a)>=3:
        b=a[3:-3]
        c=b[-1]+b[:-1]
    else:
        c=a[::-1]
    print("Your decoded message is: ", c)