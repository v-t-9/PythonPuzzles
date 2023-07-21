# Write a Python program to find numbers that are greater than 10 and have odd first and last digits.
# Input:
l1 = [1, 3, 79, 10, 4, 1, 39, 62]
# Output:
# [79, 39]
# Input:
l2 = [11, 31, 77, 93, 48, 1, 57]
# Output:
# [11, 31, 77, 93, 57]

def odd_first_and_last(l):
    d = []
    odd = []
    res = []
    x = []
    for i in l:
        if i > 10:
            d.append(list(map(int, str(i))))
    for i in d:
        if i[0] % 2 != 0 and i[len(i)-1] % 2 !=0 :
            odd.append(list(map(str, i)))
    x = [''.join([str(j) for j in i]) for i in odd]

    res = [int(i) for i in x]
    return res

if __name__ == "__main__":
    print(odd_first_and_last(l1))
    print(odd_first_and_last(l2))
