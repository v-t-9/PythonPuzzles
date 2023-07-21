# Write a Python program to find the product of the units digits in the numbers in a given list.
n1 = 10
# Output:
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
n2 = 15
# Output:
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
n3 = 50
# Output:
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976, 7778742049, 12586269025]

def product_units_digits(n):
    n1= 1
    n2=1
    num = 0
    res = [n1, n2]
    for i in range(2,n,1):
        num = n1 + n2
        res.append(num)
        n1 = n2
        n2 = num
    return res

if __name__ == "__main__":
    print(product_units_digits(n1))
    print(product_units_digits(n2))
    print(product_units_digits(n3))