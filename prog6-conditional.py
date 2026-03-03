# a = int(input("Enter your age: ") )
# print("Your age is:", a)
# if(a>18):
#     print("You can drive")
#     print("Yes")
# elif(a==18):
#     print("You are exactly 18 years old")
# else:
#     if(a<10):
#         print("You are too young to drive")
#     else:    
#         print("You cannot drive")
# print("Yay!")#indentation does not matter here as it is not a part of the if-else block

# A program to wish good morning, good afternoon or good evening based on the time of the day
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)

timestamp = time.strftime('%H')
if(int(timestamp)<12):
    print("Good Morning")   
elif(int(timestamp)<18):
    print("Good Afternoon")
else:
    print("Good Evening")


