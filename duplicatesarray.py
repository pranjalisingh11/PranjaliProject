arr = list(map(int, input("Enter the array elements: ").split()))

unique_elements = set()
duplicates = set()

for elements in arr:
    if elements in unique_elements:
        duplicates.add(elements)
    else:
        unique_elements.add(elements)

print("Duplicate elements present in array are: ")
for elements in duplicates:
    print(elements)