# Write a Python program to find all even palindromes up to n.
# Output:
# Even palindromes up to 50 -
# [0, 2, 4, 6, 8, 22, 44]
# Even palindromes up to 100 -
# [0, 2, 4, 6, 8, 22, 44, 66, 88]
# Even palindromes up to 500 -
# [0, 2, 4, 6, 8, 22, 44, 66, 88, 202, 212, 222, 232, 242, 252, 262, 272, 282, 292, 404, 414, 424, 434, 444, 454, 464, 474, 484, 494]
# Even palindromes up to 2000 -
# [0, 2, 4, 6, 8, 22, 44, 66, 88, 202, 212, 222, 232, 242, 252, 262, 272, 282, 292, 404, 414, 424, 434, 444, 454, 464, 474, 484, 494, 606, 616, 626, 636, 646, 656, 666, 676, 686, 696, 808, 818, 828, 838, 848, 858, 868, 878, 888, 898]

n1 = 50
n2 = 100
n3 = 500
n4 = 2000

def even(n):
    even= []
    for i in range(n):
        if i % 2 == 0:
            even.append(i)
    return even

def even_palindromes(n):
    l = even(n)
    res = []
    for i in range(len(l)):
        num = str(l[i])
        if num == num[::-1]:
           res.append(l[i])
    return res

if __name__ == "__main__":
    print(even_palindromes(n1))
    print(even_palindromes(n2))
    print(even_palindromes(n3))
    print(even_palindromes(n4))
