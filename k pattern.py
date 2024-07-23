n = int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(n+1,i,-1):
        print("*",end=" ")
    print()
for i in range(2,n+2):
    print("* "*i,end=" ")
    print()
