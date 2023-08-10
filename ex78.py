from ex66 import closest_pair
#  Write a Python program to find the two closest distinct numbers in a given list of numbers.
# Input:
l1 = [1.3, 5.24, 0.89, 21.0, 5.27, 1.3]
# Output:
# [5.24, 5.27]
# Input:
l2 = [12.02, 20.3, 15.0, 19.0, 11.0, 14.99, 17.0, 17.0, 14.4, 16.8]
# Output:
# [14.99, 15.0]


def closest_numbers(l):
    l1 = list(set(l))
    ind = closest_pair(l1)
    res = [l1[i] for i in ind]
    return res


if __name__ == "__main__":
    l1 = [1.3, 5.24, 0.89, 21.0, 5.27, 1.3]
    l2 = [12.02, 20.3, 15.0, 19.0, 11.0, 14.99, 17.0, 17.0, 14.4, 16.8]

    print(closest_numbers(l1))
    print(closest_numbers(l2))
