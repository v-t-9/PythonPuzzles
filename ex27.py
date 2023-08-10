# Write a Python program to find x that minimizes the mean squared deviation from a given 
# list of numbers.
# Input:
# l1 = [4, -5, 17, -9, 14, 108, -9]
# Output:
# 17.142857142857142
# Input:
# l2= [12, -2, 14, 3, -15, 10, -45, 3, 30]
# Output:
# 1.1111111111111112

def meanSquaredDeviation(l):
    d = sum(l)/len(l)
    return d

if __name__ == "__main__":
    l1 = [4, -5, 17, -9, 14, 108, -9]
    l2= [12, -2, 14, 3, -15, 10, -45, 3, 30]
    print(meanSquaredDeviation(l1))
    print(meanSquaredDeviation(l2))