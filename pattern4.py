n = int(input("enter any number: "))
for i in range(n,0,-1):
    print(chr(65 + i-1) * i)