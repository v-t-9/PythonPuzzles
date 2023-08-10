# Write a Python program to find the vowels from each of the original texts (y counts as a vowel at the end of the word) from a given list of strings.
# l1 = ['w3resource', 'Python', 'Java', 'C++']
# Output:
# ['eoue', 'o', 'aa', '']
# l2 = ['ably', 'abruptly', 'abecedary', 'apparently', 'acknowledgedly']
# Output:
# ['ay', 'auy', 'aeeay', 'aaey', 'aoeey']

def vowels(l):
    res = []
    list1 = [i.lower() for i in l]
    res = ["".join(j for j in i if j in "aeiou") + (i[-1] if i[-1]=="y" else "") for i in list1]
  
    return res

if __name__ == "__main__":
    l1 = ['w3resource', 'Python', 'Java', 'C++']
    l2 = ['ably', 'abruptly', 'abecedary', 'apparently', 'acknowledgedly']
    print(vowels(l1))
    print(vowels(l2))