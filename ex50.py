# Write a Python program to find even-length words from a given list of words and sort them by length.
# Original list of words:
l1 = ['Red', 'Black', 'White', 'Green', 'Pink', 'Orange']
# Find the even-length words and sort them by length in the said list of words:
# ['Pink', 'Orange']
# Original list of words:
l2 = ['The', 'worm', 'ate', 'a', 'bird', 'imagine', 'that', '!', 'Absurd', '!!']
# Find the even-length words and sort them by length in the said list of words:
# ['!!', 'bird', 'that', 'worm', 'Absurd']

def even_words(l):
    leng = []
    res = []
    for i in l:
        leng.append(len(i))
    for i in range(len(leng)):
        if leng[i] % 2 == 0:
                res.append(l[i])
    res.sort(key=len)
    return res

if __name__ == "__main__":
    print(even_words(l1))
    print(even_words(l2))
