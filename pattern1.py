n = int(input("enter a number: "))

for i in range(1,n+1):
    for j in range(65,65+i):
        print(chr(j),end="")
    print()
