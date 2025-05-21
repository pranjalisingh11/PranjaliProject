def is_reverse(num):

    rev = 0
    while num > 0:
        id = num % 10
        rev = rev * 10 + id
        num = num // 10
    return rev

num = int(input("Enter any number: "))
rev = is_reverse(num)
print(f"the reverse number is: {rev}")