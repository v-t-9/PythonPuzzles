# Write a Python program to find the sublist of numbers from a given list of numbers with only odd digits in increasing order.
# Input:
l1 = [1, 3, 79, 10, 4, 2, 39]
# Output:
# [1, 3, 39, 79]
# Input:
l2 = [11, 31, 40, 68, 77, 93, 48, 1, 57]
# Output:
# [1, 11, 31, 57, 77, 93]
# Input:
l3 = [9, -2, 3, 4, -2, 0, 2, -3, 8, -1]
# Output:
# [-3, -1, 3, 9]

def odd_increasing(l):
    res = sorted([i for i in l if i % 2 != 0])
    return res


if __name__ == "__main__":
    print(odd_increasing(l1))
    print(odd_increasing(l2))
    print(odd_increasing(l3))