# Write a Python program to calculate the average of the numbers a through b (b not included) rounded to the nearest integer, in binary (or -1 if there are no such numbers).
# Input:
# n1 = 4
# n2 = 7
# Output:
# 0b101
# Input:
# n3 = 11 
# n4 = 19
# Output:
# 0b1110

def avg_bin(a, b):
    l = [ i for i in range(a,b)]
    avg = round(sum(l)/len(l))
    b_avg = bin(avg)
    return b_avg

if __name__ == "__main__":
    n1 = 4
    n2 = 7
    n3 = 11 
    n4 = 19
    print(avg_bin(n1,n2))
    print(avg_bin(n3,n4))