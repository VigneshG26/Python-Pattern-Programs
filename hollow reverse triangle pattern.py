n= int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(1,i):
        print(end=" ")
    for j in range(n,i-1,-1):
        if(j==n or j==i or i==1):
            print("*",end= " ")
        else:
            print(end="  ")
    print()
