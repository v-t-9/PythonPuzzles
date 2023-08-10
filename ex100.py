# Write a Python program to find four positive even integers whose sum is a given integer.
# Input:
# n1 = 100
# Output:
# [94, 2, 2, 2]
# Input:
# n2 = 1000
# Output:
# [994, 2, 2, 2]
# Input:
# n3 = 10000
# Output:
# [9994, 2, 2, 2]
# Input:
# n4 = 1234567890
# Output:
# [1234567884, 2, 2, 2]

def sum_even_int(n):
    
    res = [ i for i in range(1,7) if i % 2 == 0]
    r = n-sum(res)
    res.append(r)
    return res

if __name__ == "__main__":
    n1 =  100
    n2 = 1000
    n3 = 10000
    n4 = 1234567890
    print(sum_even_int(n1))
    print(sum_even_int(n2))
    print(sum_even_int(n3))
    print(sum_even_int(n4))
