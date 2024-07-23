n = int(input("Enter a number: "))
val1 = (n * 2) - 1

for i in range(1, n + 1):
    val1 = val1 - 2
    for j in range(0, i):
        print("*", end=" ")
    for j in range(val1, 0, -1):
        print(end=" ")
    for j in range(val1, 0, -1):
        print(end=" ")
    if i == n:
        i = i-1
    print("* "*i, end=" ")
    print()

val2 = -1
for i in range(1, n):
    val2 = val2 + 2
    for j in range(n - i, 0, -1):
        print("*", end=" ")
    for j in range(0, val2):
        print(end=" ")
    for j in range(0, val2):
        print(end=" ")
    for j in range(n - i, 0, -1):
        print("*", end=" ")
    print()
