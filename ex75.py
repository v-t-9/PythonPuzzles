# Write a Python program to reorder numbers from a given array in increasing/decreasing order based on whether the first plus last element is odd/even.
# Reorder numbers of a give array in increasing/decreasing order based on whether the first plus last element is odd/even.:
# Input:
l1 = [3, 7, 4]
# Output:
# [3, 4, 7]
# Input:
l2 = [2, 7, 4]
# Output:
# [7, 4, 2]
# Input:
l3 = [1, 5, 6, 7, 4, 2, 8]
# Output:
# [1, 2, 4, 5, 6, 7, 8]
# Input:
l4 = [1, 5, 6, 7, 4, 2, 9]
# Output:
# [9, 7, 6, 5, 4, 2, 1]

def reorder(l):
    su = l[0] + l[-1]
    res = []
    if su % 2 != 0:
        res = sorted(l)
        return res
    else:
        res = sorted(l, reverse=True)
        return res
print(reorder(l1))
print(reorder(l2))
print(reorder(l3))
print(reorder(l4))