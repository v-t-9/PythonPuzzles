# Write a Python program to find the indices of the closest pair from a list of numbers.
l1 = [1, 7, 9, 2, 10]
# Output:
# [0, 3]
l2 = [1.1, 4.25, 0.79, 1.0, 4.23]
# Output:
# [4, 1]
l3 = [0.21, 11.3, 2.01, 8.0, 10.0, 3.0, 15.2]
# Output:
# [2, 5]

def closest_pair(l):
    res = []
    num = []
    sorted_list = sorted(l)   
   
    diff = [ sorted_list[i] - sorted_list[i-1] for i in range(len(sorted_list))]
    diff.pop(0)
    diff.insert(0, 1000)

    mi = min(diff)

    for i in range(len(diff)):
        if diff[i] == mi:
            num.append(sorted_list[i])
            num.append(sorted_list[i -1])

    res = [l.index(i) for i in sorted(num)]

    return res
if __name__ == "__main__":
    print(closest_pair(l1))
    print(closest_pair(l2))
    print(closest_pair(l3))