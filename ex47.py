# Write a Python program to filter for numbers in a given list whose sum of digits is > 0, where the first digit can be negative.
# Input:
l1 = [11, -6, -103, -200]
# Output:
# [11, -103]
# Input:
l2 = [1, 7, -4, 4, -9, 2]
# Output:
# [1, 7, 4, 2]
# Input:
l3 = [10, -11, -71, -13, 14, -32]
# Output:
# [10, -13, 14]


def filter_digits(l):
     res =[]
     for num in l:
        neg = num < 0  
        if neg:
            v1 = int(str(num)[1]) 
        num = str(abs(num)) 
        sum_n = sum(int(i) for i in num) 
        if neg:
            sum_n = sum_n - 2*v1  
        res.append(sum_n)
     return res

def moreThanZero(l):
    li = filter_digits(l)
    res = []
    for i in range(len(li)):
        if li[i] >0:
            res.append(l[i])
    return res
print(moreThanZero(l1))
print(moreThanZero(l2))
print(moreThanZero(l3))