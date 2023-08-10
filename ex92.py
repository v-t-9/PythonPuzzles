# Write a Python program to start with a list of integers, keep every other element in place and otherwise sort the list.
# Input:
# l1 = [2, 5, 6, 3, 1, 4, 34]
# Output:
# [1, 5, 2, 3, 6, 4, 34]
# Input:
# l2 = [8, 0, 7, 2, 9, 4, 1, 2, 8, 3]
# Output:
# [1, 0, 7, 2, 8, 4, 8, 2, 9, 3]

def int_sort(l):
    res = []
    a = [ l[i] for i in range(len(l)) if i%2!=0 ]
    b = sorted([ l[i] for i in range(len(l)) if i%2==0 ] )
    if len(a)>len(b):
        b.append(None)
    if len(a)<len(b):
        a.append(None)
    r = list(zip(b,a))
    for i in r:
        for j in i:
            if j != None:
                res.append(j)
    return res


if __name__ == "__main__":
    l1 = [2, 5, 6, 3, 1, 4, 34]
    l2 = [8, 0, 7, 2, 9, 4, 1, 2, 8, 3]
    print(int_sort(l1))
    print(int_sort(l2))
