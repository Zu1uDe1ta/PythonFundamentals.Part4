
n = int(input())

def Fibonacci(n):
    if n<0:
        print("Invalid Number")
    elif n>30:
        print("Invalid Number")
    elif n==1:
        print(0)
    elif n==2:
        print(1)
    else:
        print((n-1)+(n-2))
Fibonacci(n)
