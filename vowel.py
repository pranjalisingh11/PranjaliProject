def find_vowels(str):
    vowels = "aeiouAEIOU"
    found_vowels = []

    for char in str:
        if char in vowels and char not in found_vowels:
            found_vowels.append(char)

    return found_vowels

str = input("enter any string: ")
found_vowels = find_vowels(str)

if found_vowels:
    print(f"Vowels in the given string are: {', '.join(found_vowels)}")
else:
    print("No vowels found in the given string.")
