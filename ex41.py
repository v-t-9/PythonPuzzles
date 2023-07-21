# Write a Python program to sort numbers based on strings.
s1 = "six one four one two three"
# Output:
# one two three four six
s2 = "six one four three two nine eight"
# Output:
# one two three four six eight nine
s3 = "nine eight seven six five four three two one"
# Output:
# one two three four five six seven eight nine

def wordToNum(s):
    dic = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    num = []
    res = ""
    l = s.split(" ")
    for i in l:
        if i in dic.keys():
            num.append(dic[i])
    sorted_num = sorted(num)
    for key, value in dic.items():
        if value in sorted_num:
            res = res + " " +key

    return res

if __name__ == "__main__":
    print(wordToNum(s1))
    print(wordToNum(s2))
    print(wordToNum(s3))