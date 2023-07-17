# Given a list of numbers and a number to inject, write a Python program to create a list containing that number in between each pair of adjacent numbers.
l1 = [12, -7, 3, -89, 14, 88, -78, -1, 2, 7]
sep1 = 6
# Output:
# [12, 6, -7, 6, 3, 6, -89, 6, 14, 6, 88, 6, -78, 6, -1, 6, 2, 6, 7]
l2 = [1, 2, 3, 4, 5, 6]
sep2 = 9
# Output:
# [1, 9, 2, 9, 3, 9, 4, 9, 5, 9, 6]

def num_between_pair(l, sep):
    l1 = [ [i , sep] for i in l]
    res = [ j for i in l1 for j in i]
    return res[:len(res)-1]
print(num_between_pair(l1, sep1))
print(num_between_pair(l2, sep2))