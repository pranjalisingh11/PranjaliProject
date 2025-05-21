def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num%i != 0:
            return True
        else:
            return False

num = int(input("Enter any number:"))
if is_prime(num):
    print(f"{num} is prime number")
else:
    print(f"{num} is not prime number")