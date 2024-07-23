n = int(input("Enter a number: "))
val = 0
for i in range(1,n+1):
    if i%2 == 0:
            val = 0
    else:
        val = 1
    for j in range(0,i):
        print(val, end=" ")
        if val == 0:
            val = 1
        else:
            val = 0
    print()
