# this to print the factorial of a number


# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
    
def trailingoffactorial(n):
    i=5
    cout=0
    while(n//i!=0):
        cout+=int(n/i)
        i*=5
    return cout

n=int(input("enter a number of which you want to find the factorial:"))
# factorial(n)
trailingoffactorial(n)
# print(factorial(n))
print(trailingoffactorial(n))

