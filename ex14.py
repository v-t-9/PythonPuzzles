# Write a Python program to find the length of a given list of non-empty strings.
# Input: ['cat', 'car', 'fear', 'center']
# Output:
# [3, 3, 4, 6]
# Input:  ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
# Output:
# [3, 3, 7, 5, 2, 4, 0]
 
def lengthString(l):
    lengths = []
    for i in l:
        lengths.append(len(i))
    return lengths

if __name__ == "__main__":
    l1 = ['cat', 'car', 'fear', 'center']
    l2 = ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
    print(lengthString(l1))
    print(lengthString(l2))