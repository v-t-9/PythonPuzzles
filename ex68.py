# Write a Python program to find all 5's in integers less than n that are divisible by 9 or 15.
# Input:
# n1 = 50
# Output:
# [[15, 1], [45, 1]]
# Input:
# n2 = 65
# Output:
# [[15, 1], [45, 1], [54, 0]]
# Input:
# n3 = 75
# Output:
# [[15, 1], [45, 1], [54, 0]]
# Input:
# n4 = 85
# Output:
# [[15, 1], [45, 1], [54, 0], [75, 1]]
# Input:
# n5 = 150
# Output:
# [[15, 1], [45, 1], [54, 0], [75, 1], [105, 2], [135, 2]]

def divisible_by_9_or_15(n):
    l = [ i for i in range(0,n) if "5" in str(i)]
    div = [str(l[i]) for i in range(len(l)) if l[i] % 15 == 0 or l[i] % 9 == 0]
    res = [[int(i),j] for i in div for j in range(len(i)) if i[j] == "5"]
    return res

if __name__ == "__main__":
    n1 = 50
    n2 = 65
    n3 = 75
    n4 = 85
    n5 = 150

    print(divisible_by_9_or_15(n1))
    print(divisible_by_9_or_15(n2))
    print(divisible_by_9_or_15(n3))
    print(divisible_by_9_or_15(n4))
    print(divisible_by_9_or_15(n5))