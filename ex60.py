# Write a Python program to find a list of all numbers that are adjacent to a prime number
# in the list, sorted without duplicates.
# Input:
l1 = [2, 17, 16, 0, 6, 4, 5]
# Output:  
# [2, 4, 16, 17]
# Input:
l2 = [1, 2, 19, 16, 6, 4, 10]
# Output:
# l3 = [1, 2, 16, 19]
# Input:
l3 = [1, 2, 3, 5, 1, 16, 7, 11, 4]
# Output:
# [1, 2, 3, 4, 5, 7, 11, 16]

def Prime(l):
    res = []
    for i in l:
        c = 0
        for j in range(1,i):
            if i %j == 0:
                c = c +1
        if c == 1:
            res.append(True)
        else:
            res.append(False)
    return res

def adjacent_to_prime(l):
    p = Prime(l)
    res = []
    mi_pos = []
    ma_pos = []
    for i in range(len(p)):
        if p[i] == True:
            if i > 0:
                mi_pos.append(i-1)
            ma_pos.append(i+1)

    for i in range(len(l)):
        if i in mi_pos:
            res.append(l[i])
        if i in ma_pos:
            res.append(l[i])
    
    res1 = set(res)
    res = list(res1)
    res.sort()
    return res
if __name__ == "__main__":
    print(adjacent_to_prime(l1))
    print(adjacent_to_prime(l2))
    print(adjacent_to_prime(l3))


