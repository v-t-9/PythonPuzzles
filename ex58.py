#  Write a Python program to find the biggest even number between two numbers inclusive.
# Input:
# m1 = 12
# n1 = 51
# Output:
# 50
# Input:
# m2 = 1
# n2 = 79
# Output:
# 78
# Input:
# m3 = 47
# n3 = 53
# Output:
# 52
# Input:
# m4 = 100
# n4 = 200
# Output:
# 200

def biggest_even_number(m,n):
    for i in range(n, m, -1):
        if i % 2 == 0:
            return i

if __name__ == "__main__":
    m1 = 12
    n1 = 51
    m2 = 1
    n2 = 79
    m3 = 47
    n3 = 53
    m4 = 100
    n4 = 200
    
    print(biggest_even_number(m1, n1))
    print(biggest_even_number(m2, n2))
    print(biggest_even_number(m3, n3))
    print(biggest_even_number(m4, n4))