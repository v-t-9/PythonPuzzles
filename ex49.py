# Write a Python program to find the h-index, the largest positive number h such that h occurs 
# in the sequence at least h times. If there is no such positive number return h = -1.
# Input:
l1 = [1, 2, 2, 3, 3, 4, 4, 4, 4]
# Output:
# 4
# Input:
l2 = [1, 2, 2, 3, 4, 5, 6]
# Output:
# 2
# Input:
l3 = [3, 1, 4, 17, 5, 17, 2, 1, 41, 32, 2, 5, 5, 5, 5]
# Output:
# 5

def frecuency(l):
    for i in l:
        if max(l):
            if i > 0 and l.count(i) >= i:
                h = i
        else:
            h = -1
    return h
print(frecuency(l1))
print(frecuency(l2))
print(frecuency(l3))

