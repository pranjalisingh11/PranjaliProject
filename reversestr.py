#str = input("Enter any string: ")
#reversed_str = str[::-1]
#print(reversed_str)

str = input("Enter any string: ")
i = len(str)-1
output = ""
while i >= 0:
    output = output + str[i]
    i = i - 1
print(output)