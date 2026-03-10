# Factorial 7 is 7*6*5*4*3*2*1 = 5040
#the 10 fibonacci numbers are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
def fact(n):
    if(n==0 or n==1):
        return 1
    else :
        return n*fact(n-1)
print("The factorial of 7 is:", fact(7))

def fibo(n):
    if(n==1):
        return 0
    elif(n==2):
        return 1
    else:
        return(fibo(n-1)+fibo(n-2))
    
print("The 10th term of the Fibonacci sequence is:", fibo(10))