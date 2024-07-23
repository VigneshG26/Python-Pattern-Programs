n= int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(n,i,-1):
        print(end=" ")
    for j in range(1,i+1):
        if(j==1 or i==j):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
for i in range(1,n):
    for j in range(1,i+1):
        print(end=" ")
    for j in range(n,i,-1):
        if(j==n or j==i+1):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
