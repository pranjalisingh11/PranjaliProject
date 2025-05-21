def sum_first_last(num):
    num_str = str(num)

    first_digit = int(num_str[0])
    last_digit = int(num_str[-1])

    return first_digit + last_digit

num = int(input("enter a number: "))
result = sum_first_last(num)
print(f"The sum of the first and last digits of {num} is: {result}")

