n = int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(1,i):
        print(end=" ")
    for j in range(0,4):
        print("*", end = " ")
    print()
    
