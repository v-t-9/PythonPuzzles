# Write a Python program to find the first negative balance from a given list of numbers that represent bank deposits and withdrawals.
# Input:
l1 = [[12, -7, 3, -89, 14, 88, -78], [-1, 2, 7]]
# Output:
# [-81, -1]
# Input:
l2 = [[1200, 100, -900], [100, 100, -2400]]
# Output:
# [None, -2200]

def negative_balance(l):
    res = []
    for i in l:
        r = 0
        for j in i:
            r = r + j
            if r < 0:
                res.append(r)
                break
        else:
            res.append(None)
    return res
print(negative_balance(l1))
print(negative_balance(l2))