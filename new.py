n=6
for i in range(1,n):
    for j in range(1,i+1):
        print(" "*(n-i),"*"*((2*i)-1),end="")
        break
    print("\n")

    