# Write a Python program to find the sum of the magnitudes of the elements in the array. 
# This sum should have a sign that is equal to the product of the signs of the entries.
# Input:
l1 = [1, 3, -2]
# Output:
# -6
# Input:
l2 = [1, -3, 3]
# Output:
# -7
# Input:
l3 = [10, 32, 3]
# Output:
# 45
# Input:
l4 = [-25, -12, -23]
# Output:
# -60

def sum_of_magnitudes(l):
    for i in l:
        if i < 0:
            sumnum = [ - sum(abs(i) if i < 0 else i for i in l)]
            return sumnum
    else:
        sumnum = [ sum(abs(i) if i < 0 else i for i in l)]
        return sumnum
    
print(sum_of_magnitudes(l1))
print(sum_of_magnitudes(l2))
print(sum_of_magnitudes(l3))
print(sum_of_magnitudes(l4))