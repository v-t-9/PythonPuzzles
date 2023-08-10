# Write a Python program to find an integer exponent x such that a^x = n.
# Input:
# a1 = 2 
# n1 = 1024
# Output:
# 10
# Input:
# a2 = 3 
# n2 = 81
# Output:
# 4
# Input:
# a3 = 3 
# n3 = 1290070078170102666248196035845070394933441741644993085810116441344597492642263849
# Output:
# 170

def exponent(a,n):
    b = 1
    count = 0
    while b < n:
        b = b * a
        count = count + 1
    return count

if __name__ == "__main__":
    a1 = 2 
    n1 = 1024
    a2 = 3 
    n2 = 81
    a3 = 3 
    n3 = 1290070078170102666248196035845070394933441741644993085810116441344597492642263849
    print(exponent(a1, n1))
    print(exponent(a2, n2))
    print(exponent(a3, n3))