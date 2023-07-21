# An irregular/uneven matrix, or ragged matrix, is a matrix that has a different number of elements in each row. Ragged matrices are not used in linear algebra, since standard matrix transformations cannot be performed on them, but they are useful as arrays in computing.
# Write a Python program to find the indices of all occurrences of target in the uneven matrix.
# Input:
t1 =([1, 3, 2, 32, 19], [19, 2, 48, 19], [], [9, 35, 4], [3, 19])
target1 = 19
# Output:
# [[0, 4], [1, 0], [1, 3], [4, 1]]
# Input:
t2 = ([1, 2, 3, 2], [], [7, 9, 2, 1, 4])
target2 = 2
# Output:
# [[0, 1], [0, 3], [2, 2]]

def raggedMatrix(t, tar):
    l = list(t)
    res = ""
    lres = []
    r = []
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j] == tar:
                res = i , j 
                lres = list(res)
                r.append(lres)
    return r

if __name__ == "__main__":
    print(raggedMatrix(t1,target1))
    print(raggedMatrix(t2,target2))
