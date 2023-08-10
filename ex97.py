# Write a Python program to find the following strange sort of list of numbers: 
# the first element is the smallest, the second is the largest of the remaining, the third is the smallest of the remaining, the fourth is the smallest of the remaining, etc.
# Input:
# l1 = [1, 3, 4, 5, 11]
# Output:
# [1, 11, 3, 5, 4]
# Input:
# l2 = [27, 3, 8, 5, 1, 31]
# Output:
# [1, 31, 3, 27, 5, 8]
# Input:
# l3 = [1, 2, 7, 3, 4, 5, 6]
# Output:
# [1, 7, 2, 6, 3, 5, 4]

def strange_sort(l):
    x = sorted(l)
    leng = len(x)
    res1 = []
    res2 = []
    res = []
    for i in range(leng):
        res1.append(x[i])
        res2.append(x[-i])
    a = list(zip(res2, res1))
    for i in a:
        for j in i:
            if j not in res:
                res.append(j)
    
    return res

if __name__ == "__main__":
    l1 = [1, 3, 4, 5, 11]
    l2 = [27, 3, 8, 5, 1, 31]
    l3 = [1, 2, 7, 3, 4, 5, 6]
    print(strange_sort(l1))
    print(strange_sort(l2))
    print(strange_sort(l3))