def greatest_number(arr):
    if not arr:
        return None

    greatest = arr[0]
    for num in arr:
        if num > greatest:
            greatest = num

    return greatest

arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
greatest = greatest_number(arr)
if greatest is not None:
    print(f"The greatest number in the array is: {greatest}")
else:
    print("Array is empty")
