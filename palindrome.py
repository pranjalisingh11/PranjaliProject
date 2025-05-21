def is_palindrome(n):
    rev = 0
    temp = n

    while temp != 0:
        id = temp % 10
        rev = rev * 10 + id
        temp = temp // 10
    return rev == n

n = int(input("Enter any number: "))
if is_palindrome(n):
    print(f"{n} is a palindrome number")
else:
    print(f"{n} is not a palindrome number")
