#the else block in a for loop is executed only when the for loop has completed its execution without encountering a break statement.
#  If the for loop is not executed at all (for example, if the range is empty), the else block will still be executed.
i=0
for i in range(5):
    print(i)
else:
    print("The for loop has completed its execution")
print(i) # This will print the value of i after the for loop. Since the for loop is not executed, the value of i will be 0, which is the initial value assigned to it before the for loop.

for j in range(1,7):
    if(j==4):
        break
    print(j)
else:
    print("The for loop has completed its execution ") # This will not be executed because the for loop is terminated by the break statement when j is equal to 4. If there were no break statement, this else block would be executed after the for loop completes its execution.           
print("\n") # This will print a newline character to separate the output of the two loops.
i=0
while i<5:
    print(i)
    i+=1  
    if i==3:  
        break   
else:
    print("The while loop has completed its execution") # This will not be executed because the while loop is terminated by the break statement when i is equal to 3. If there were no break statement, this else block would be executed after the while loop completes its execution.