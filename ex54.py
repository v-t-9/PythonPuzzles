#  Write a Python program to remove duplicates from a list of integers, preserving order.
# Input:
l1 = [1, 3, 4, 10, 4, 1, 43]
# Output:
# [1, 3, 4, 10, 43]
# Input:
l2 = [10, 11, 13, 23, 11, 25, 23, 76, 99]
# Output:
# [10, 11, 13, 23, 25, 76, 99]

def duplicates(l):
    res = []
    for i in l:
        if i not in res:
            res.append(i)
    return res
if __name__ == "__main__":
    print(duplicates(l1))
    print(duplicates(l2))
