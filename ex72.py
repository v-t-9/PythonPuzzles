# Write a Python program to find the indices of three numbers that sum to 0 in a given list of numbers.
l1 =[12, -7, 3, -89, 14, 4, -78, -1, 2, 7]
# Output:
# [1, 2, 5]
l2 =[1, 2, 3, 4, 5, 6, -7]
# Output:
# [2, 3, 6]

def indeces_sum_0(l):
    res = []
    
    for i in range(len(l)-2):           
        for j in range(i+1, len(l)-1):
            for k in range(j+1, len(l)):
                if l[i] + l[j] + l[k] == 0:
                    r = []
                    r.append(i)
                    r.append(j)
                    r.append(k)
                    res.append(r)
    return res
print(indeces_sum_0(l1))
print(indeces_sum_0(l2))
