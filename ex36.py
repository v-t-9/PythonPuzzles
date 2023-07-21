# Write a Python program to find the largest k numbers from a given list of numbers.
l = [1, 2, 3, 4, 5, 5, 3, 6, 2]
k1 = 1
# Output:
# [6]
# Input:  [1, 2, 3, 4, 5, 5, 3, 6, 2]
k2 = 2
# Output:
# [6, 5]
# Input: [1, 2, 3, 4, 5, 5, 3, 6, 2]
k3 = 3
# Output:
# [6, 5, 5]
# Input:  [1, 2, 3, 4, 5, 5, 3, 6, 2]
k4 = 4
# Output:
# [6, 5, 5, 4]
# Input: [1, 2, 3, 4, 5, 5, 3, 6, 2]
k5 = 5
# Output:
# [6, 5, 5, 4, 3]

def largestNum(l, k):
    s = sorted(l)
    r = s[::-1]
    res = []
    for i in range(k):
        res.append(r[i])
    return res

if __name__ == "__main__":
    print(largestNum(l ,k1))
    print(largestNum(l ,k2))
    print(largestNum(l ,k3))
    print(largestNum(l ,k4))
    print(largestNum(l ,k5))