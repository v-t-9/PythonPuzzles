# Write a Python program to find the indices of two entries that show that the list is not 
#in increasing order. If there are no violations (they are increasing), return an empty list.
# Input:
l1 = [1, 2, 3, 0, 4, 5, 6]
# Output:
# [2, 3]
# Input:
l2 = [1, 2, 3, 4, 5, 6]
# Output:
# []
# Input:
l3 = [1, 2, 3, 4, 6, 5, 7]
# Output:
# [4, 5]
# Input:
l4 = [-3, -2, -3, 0, 2, 3, 4]
# Output:
# [1, 2]

def not_increasing_order(l):
    group = list(zip(l, l[1:]))
    li = []
    res = []
    item = []
    for i in group:
        li.append(list(i))
    for i in li:
        for j in range(len(i)):
            if not i[j] < i[j-1]:
                item.append(i)
            break

    if item == []:
        return []
    else:
        for i in range(len(li)):
            
            if li[i] in item:
                res.append(i)
                res.append(i+1)
        return res
    
  
print(not_increasing_order(l1))
print(not_increasing_order(l2))
print(not_increasing_order(l3))
print(not_increasing_order(l4))
