# Write a Python program to find the length of a given list of non-empty strings.
# Input:
l1 = ['cat', 'car', 'fear', 'center']
# Output:
# [3, 3, 4, 6]
# Input:
l2 = ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
# Output:
# [3, 3, 7, 5, 2, 4, 0]
 
def lengthString(l):
    lengths = []
    for i in l:
        lengths.append(len(i))
    return lengths
print(lengthString(l1))
print(lengthString(l2))