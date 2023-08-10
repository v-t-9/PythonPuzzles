from ex60 import Prime
# Write a Python program to find the index of the largest prime in the list and the sum 
# of its digits.
# l1 = [3, 7, 4]
# Output:
# [1, 7]
# l2 = [3, 11, 7, 17, 19, 4]
# Output:
# [4, 10]
# l3 = [23, 17, 201, 14, 10473, 43225, 421, 423, 11, 10, 2022, 342157]
# Output:
# [6, 7]

def largest_prime_sum(l):
    p = Prime(l)
    p2 = []
    for i in range(len(p)):
        if p[i] == True:
          p2.append(l[i])
    ma = max(p2)
    s = str(ma)
    if len(s) > 1: 
        su = sum(int(i) for i in s)
        return [l.index(ma), su]
    else:
        return [l.index(ma), ma]
    
if __name__ == "__main__":
    l1 = [3, 7, 4]
    l2 = [3, 11, 7, 17, 19, 4]
    l3 = [23, 17, 201, 14, 10473, 43225, 421, 423, 11, 10, 2022, 342157]
    print(largest_prime_sum(l1))
    print(largest_prime_sum(l2))
    print(largest_prime_sum(l3))