# Write a Python program to find the indices of two numbers that sum to 0 in a given list of numbers.
# Input:
l1 = [1, -4, 6, 7, 4]
# Output:
# [4, 1]
# Input:
l2 = [1232, -20352, 12547, 12440, 741, 341, 525, 20352, 91, 20]
# Output:   
# [1, 7]

def sum0Indexes(l):
    r = []
    for i in l:
        if (-i) in l:
            r.append(l.index(i))
    return r

print(sum0Indexes(l1))
print(sum0Indexes(l2))