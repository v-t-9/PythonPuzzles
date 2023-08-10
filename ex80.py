import math
# Write a Python program to round each float in a given list of numbers up to the next integer and return the running total of the integer squares.
# l1 = [2.6, 3.5, 6.7, 2.3, 5.6]
# Output:
# [9, 25, 74, 83, 119]
# l2 = [301.1, 401.4, -23.1, 13554122.0, 10201.0101, 10000000.0]
# Output:
# [91204, 252808, 253337, 183714223444221, 183714327525025, 283714327525025]

def round_to_next_int(l):
    res = []
    r = 0
    round_next = [math.ceil(i)**2 for i in l]
    for i in round_next:
        r = r + i
        res.append(r)
    return res

if __name__ == "__main__":
    l1 = [2.6, 3.5, 6.7, 2.3, 5.6]
    l2 = [301.1, 401.4, -23.1, 13554122.0, 10201.0101, 10000000.0]

    print(round_to_next_int(l1))
    print(round_to_next_int(l2))