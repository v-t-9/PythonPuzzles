# Write a Python program to find the largest negative and smallest positive numbers (or 0 if none).
# Input:
l1 = [-12, -6, 300, -40, 2, 2, 3, 57, -50, -22, 12, 40, 9, 11, 18]
# Output:
# [-6, 2]
# Input:
l2 = [-1, -2, -3, -4]
# Output:
# [-1, 0]
# Input:
l3 = [1, 2, 3, 4]
# Output:
# [0, 1]
# Input:
l4 = []
# Output:
# [0, 0]

def largest_negative_smallest_positive(l):
    n = [i for i in l if i <0]
    p = [i for i in l if i>0]
    
    if n == [] and p == []:
        return [0, 0]
    if n == []:
        return [0 , min(p)]
    if p == []:
        return [max(n), 0]
    else:
        return [max(n), min(p)]

if __name__ == "__main__":
    print(largest_negative_smallest_positive(l1))
    print(largest_negative_smallest_positive(l2))
    print(largest_negative_smallest_positive(l3))
    print(largest_negative_smallest_positive(l4))
