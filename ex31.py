# 31. Write a Python program to find the coordinates of a triangle with given side lengths.
# Input:
# l1 = [3, 4, 5]
# Output:
# [[0.0, 0.0], [3, 0.0], [3.0, 4.0]]
# Input:
# l2 = [5, 6, 7]
# Output:
# [[0.0, 0.0], [5, 0.0], [3.8, 5.878775382679628]]

def coordinates(l):
    per = sum(l)
    sper = per/2
    side1, side2, side3 = sorted(l)
    ar  = (sper * (sper - side1) * (sper - side2) * (sper - side3)) ** 0.5
    y = 2 * ar / side1
    x = (side3 ** 2 - y ** 2)** 0.5

    res = [[0,0], [side1, 0], [x,y]]
    return res

if __name__ == "__main__":
    l1 = [3, 4, 5]
    l2 = [5, 6, 7]
    print(coordinates(l1))
    print(coordinates(l2))
