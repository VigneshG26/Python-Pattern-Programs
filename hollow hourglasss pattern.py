n=int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(1,i):
        print(end=" ")
    for j in range(n+1,i,-1):
        if(i==1 or j==n+1 or j==i+1):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
for i in range(1,n):
    for j in range(n-1,i,-1):
        print(end=" ")
    for j in range(2,i+3):
        if(j==2 or i==n-1 or j==i+2):
            print("*",end=" ")
        else:
            print(end="  ")
    print()

#1. shape the hourglass by fill the *
#2. print value of j instead * to find the number pattern
#3. write the logic in if condition by using the printed j value to create hollow

