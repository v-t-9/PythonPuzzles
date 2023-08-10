# Write a Python program to determine the direction ('increasing' or 'decreasing') of 
#monotonic sequence numbers.
# Input:  [1, 2, 3, 4, 5, 6]
# Output:
# Increasing.
# Input:  [6, 5, 4, 3, 2, 1]
# Output:
# Decreasing.
# Input: [19, 19, 5, 5, 5, 5, 5]
# Output:
# Not a monotonic sequence!

def direction(l):
    for i in range(len(l)):
        if l[i] < l[i+1]:
            return f"Increasing"
        elif l[i] > l[i+1]:
            return f"Decreasing"
        else:
             return f"Not a monotonic sequence"
        
if __name__ == "__main__":
    l1 = [1, 2, 3, 4, 5, 6]
    l2 = [6, 5, 4, 3, 2, 1]
    l3 = [19, 19, 5, 5, 5, 5, 5]
    print(direction(l1))
    print(direction(l2))
    print(direction(l3))