# Write a Python program to determine which triples sum to zero from a given list of lists.
l1 = [[1343532, -2920635, 332], [-27, 18, 9], [4, 0, -4], [2, 2, 2], [-20, 16, 4]]
# Output:
# [False, True, True, False, True]
l2 = [[1, 2, -3], [-4, 0, 4], [0, 1, -5], [1, 1, 1], [-2, 4, -1]]
# Output:
# [True, True, False, False, False]
def sumZero(l):
    res = []
    for i in l:
        if sum(i) == 0:
            res.append(True)
        else:
            res.append(False)
    return res
print(sumZero(l1))
print(sumZero(l2))