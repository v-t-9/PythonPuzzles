# Write a Python program to find the sum of the numbers in a given list among the first k with 
# more than 2 digits.
l1 = [4, 5, 17, 9, 14, 108, -9, 12, 76]
k1 = 4
# Output:
# 0
l2 = [4, 5, 17, 9, 14, 108, -9, 12, 76]
k2 = 6
# Output:
# 108
l3 = [114, 215, -117, 119, 14, 108, -9, 12, 76]
k3 = 5
# Output:
# 331
l4 = [114, 215, -117, 119, 14, 108, -9, 12, 76]
k4 = 1
# Output:
# 114

def sumNum(l, k):
    res = 0
    for i in l[:k]:
        if len(str(i))>2:
            res = res + i
    return res

if __name__ == "__main__":
    print(sumNum(l1,k1))
    print(sumNum(l2,k2))
    print(sumNum(l3,k3))
    print(sumNum(l4,k4))