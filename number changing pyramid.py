n = int(input("Enter a number: "))
j = 1
for i in range(2,n+2):
    for j in range(j+1,j+i):
        print(j-1, end = " ")
    print()
