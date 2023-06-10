# 7. Write a Python program to check a given list of integers where the sum of the first i integers is i.
# Input:
l1 = [0, 1, 2, 3, 4, 5]
# Output:
# False
# Input:
l2 = [1, 1, 1, 1, 1, 1]
# Output:
# True
# Input:
l3 = [2, 2, 2, 2, 2]
# Output:
# False

def sumofi(l):
    le = len(l)
    sum = 0
    for i in l:
        sum = sum + i
    if sum == le:
        return print(True)
    else:
        return print(False)
sumofi(l1)
sumofi(l2)
sumofi(l3)
sumofi([0, 1, 0, 0, 0, 5])
