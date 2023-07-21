# Write a Python program to find the number which when appended to the list makes 
# the total 0.
# Input:
l1 = [1, 2, 3, 4, 5]
# Output:
# -15
# Input:
l2 = [-1, -2, -3, -4, 5]
# Output:
# 5
# Input:
l3 = [10, 42, 17, 9, 1315182, 184, 102, 29, 15, 39, 755]
# Output:
# -1316384

sum_num = lambda l: 0 - sum(l)

if __name__ == "__main__":
    print(sum_num(l1))
    print(sum_num(l2))
    print(sum_num(l3))