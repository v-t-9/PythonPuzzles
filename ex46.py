# Given an array of numbers representing a branch on a binary tree, write a Python program to find the minimum even value and its index. In the case of a tie, return the smallest index. If there are no even numbers, the answer is [].
# Input:
l1 =[1, 9, 4, 6, 10, 11, 14, 8]
# Output:
# Minimum even value and its index of the said array of numbers:
# [4, 2]
# Input:
l2 = [1, 7, 4, 4, 9, 2]
# Output:
# Minimum even value and its index of the said array of numbers:
# [2, 5]
# Input:
l3 = [1, 7, 7, 5, 9]
# Output:
# Minimum even value and its index of the said array of numbers:
# []
def even(l):
    even = []
    for i in l:
        if i % 2 == 0:
            even.append(i)
    return even

def minValueIndex(l):
    li = even(l)
    if li == []:
        return []
    else:
        mi = min(li)
        pos = 0
        for i in range(len(l)):
            if l[i] ==mi:
                pos = i
        return [mi, pos]

print(minValueIndex(l1))
print(minValueIndex(l2))
print(minValueIndex(l3))