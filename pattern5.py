n=1
rows = int(input("Enter the number of rows: "))
for i in range(1,rows+1):
    for j in range(i):
        print(n, end=" ")
        n += 1
    print()
