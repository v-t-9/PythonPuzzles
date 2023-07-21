# Write a Python program to find the product of the units digits in the numbers in a given list.
# Input:
l1 = [12, 23]
# Output:
# 6
# Input:
l2 = [12, 23, 43]
# Output:
# 18
# Input:
l3 = [113, 234]
# Output:
# 12
# Input:
l4 = [1002, 2005]
# Output:
# 10

def product_units(l):
    res = 1
    for i in l:
        res = res * int(str(i)[-1])
    return res

    
if __name__ == "__main__":
    print(product_units(l1))
    print(product_units(l2))
    print(product_units(l3))
    print(product_units(l4))