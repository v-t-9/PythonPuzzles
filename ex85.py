# Write a Python program to find an increasing sequence consisting of the elements of the original list.
# Input:
# l1 =[1, 3, 79, 10, 4, 2, 39]
# Output:
# [1, 2, 3, 4, 10, 39, 79]
# Input:
# l2 = [11, 31, 40, 68, 77, 93, 48, 1, 57]
# Output:
# [1, 11, 31, 40, 48, 57, 68, 77, 93]
# Input:
# l3 = [9, -2, 3, 4, -2, 0, 2, -3, 8, -1]
# Output:
# [-3, -2, -1, 0, 2, 3, 4, 8, 9]
def increasing(l):
    return sorted(l)

if __name__ == "__main__":
    l1 =[1, 3, 79, 10, 4, 2, 39]
    l2 = [11, 31, 40, 68, 77, 93, 48, 1, 57]
    l3 = [9, -2, 3, 4, -2, 0, 2, -3, 8, -1]

    print(increasing(l1))
    print(increasing(l2))
    print(increasing(l3))