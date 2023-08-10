# Write a Python program to find the sum of the even elements that are at odd indices in a given list.
# Input:
# l1 = [1, 2, 3, 4, 5, 6, 7]
# Output:
# 12
# Input:
# l2 = [1, 2, 8, 3, 9, 4]
# Output:
# 6

def even_elements_odd_indices(l):
    res = [sum(l[i] for i in range(len(l)) if i % 2 !=0 and l[i] % 2 == 0)]
    return res[0]

if __name__ == "__main__":
    l1 = [1, 2, 3, 4, 5, 6, 7]
    l2 = [1, 2, 8, 3, 9, 4]
    print(even_elements_odd_indices(l1))
    print(even_elements_odd_indices(l2))