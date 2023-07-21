# Write a Python program to create a list whose ith element is the maximum of the first i elements from an input list.
# Input:
l1 = [0, -1, 3, 8, 5, 9, 8, 14, 2, 4, 3, -10, 10, 17, 41, 22, -4, -4, -15, 0]
# Output:
# [0, 0, 3, 8, 8, 9, 9, 14, 14, 14, 14, 14, 14, 17, 41, 41, 41, 41, 41, 41]
# Input:
l2 = [6, 5, 4, 3, 2, 1]
# Output:
# [6, 6, 6, 6, 6, 6]
# Input:
l3 = [1, 19, 5, 15, 5, 25, 5]
# Output:
# [1, 19, 19, 19, 19, 25, 25]

def maximum(l):
        max = l[0]
        res = []
        for i in l:
            if i>=max:
                  res.append(i)
                  max = i
            else:
                  res.append(max)
        return res


if __name__ == "__main__":
      print(maximum(l1))
      print(maximum(l2))
      print(maximum(l3))
