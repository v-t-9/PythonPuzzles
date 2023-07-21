# Write a Python program to find a list of integers containing exactly four distinct values, 
# such that no integer repeats twice consecutively among the first twenty entries.
# Input:
l1 = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
# Output:
# True
# Input:
l2 = [1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3]
# Output:
# False
# Input:
l3 = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
# Output:
# False

def distinctNonConsecutive(l):
    listUnique = []
    for i in l:
        if i not in listUnique:
            listUnique.append(i)
    if len(listUnique)>=4:
        for i in l:
            if i != (i+1):
                return True
            else:
                return False
    else:
        return False
    
if __name__ == "__main__":
    print(distinctNonConsecutive(l1))
    print(distinctNonConsecutive(l2))
    print(distinctNonConsecutive(l3))
