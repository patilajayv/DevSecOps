string = input("Enter a string: ")
unique_chars = []

for char in string:
    if char not in unique_chars:
        unique_chars.append(char)

print("Unique characters found in the string, in the order of their occurrence:")
print(unique_chars)

set1 = {20,22,24,26}
set2 = {24,26,28,30}
set3 = set1.union(set2)
set4 = set1.intersection(set2)
print(set3)
print(set4)