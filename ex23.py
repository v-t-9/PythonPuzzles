# Write a Python program to find the indices at which the numbers in the list drop.
# NOTE: You can detect multiple drops just by checking if nums[i] < nums[i-1]
# Input:
l1 = [0, -1, 3, 8, 5, 9, 8, 14, 2, 4, 3, -10, 10, 17, 41, 22, -4, -4, -15, 0]
# Output:
# [1, 4, 6, 8, 10, 11, 15, 16, 18]
# Input:
l2 = [6, 5, 4, 3, 2, 1]
# Output:
# [1, 2, 3, 4, 5]
# Input:
l3 = [1, 19, 5, 15, 5, 25, 5]
# Output:
# [0, 2, 4, 6]

def numDrop(l):
    res = []
    for i in range(len(l)):
        if l[i] < l[i-1]:
            res.append(i)
    return res

if __name__ == "__main__":
    print(numDrop(l1))
    print(numDrop(l2))
    print(numDrop(l3))