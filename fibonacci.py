n = int(input("Enter the number of terms in Fibonacci sequence: "))

if n <= 0:
    print("Please enter a positive number")
else:
    a, b  = 0, 1

    print("Fibonacci sequence: ")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a+b