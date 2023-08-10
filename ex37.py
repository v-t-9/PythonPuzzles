# Write a Python program to find the largest integer divisor of a number n 
# that is less than n.
# n1 = 18
# Output:
# 9
# n2 = 100
# Output:
# 50
# n3 = 102
# Output:
# 51
# n4 = 500
# Output:
# 250
# n5 = 1000
# Output:
# 500
# n6 = 6500
# Output:
# 3250

def largestDivisor(n):
    res = []
    for i in range(1,n):
        if n % i == 0:
            res.append(i)
    return f" The largest integer divisor of {n} is {max(res)}" 

if __name__ == "__main__":
    n1 = 18
    n2 = 100
    n3 = 102
    n4 = 500
    n5 = 1000
    n6 = 6500
    print(largestDivisor(n1))
    print(largestDivisor(n2))
    print(largestDivisor(n3))
    print(largestDivisor(n4))
    print(largestDivisor(n5))
    print(largestDivisor(n6))
