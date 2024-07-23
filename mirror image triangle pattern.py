n = int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(1,i):
        print(end=" ")
    for j in range(i,n+1):
        print(j,end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(i,i+i-1):
        print(end=" ")
    for j in range(i,n+1):
        print(j,end=" ")
    print()
