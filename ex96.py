# Write a Python program to get the single digits in numbers sorted backwards and converted into English words.
# Input:
l1 = [1, 3, 4, 5, 11]
# Output:
# ['five', 'four', 'three', 'one']
# Input:
l2 = [27, 3, 8, 5, 1, 31]
# Output:
# ['eight', 'five', 'three', 'one']

def words_digits_backwards(l):
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
    
    st = [ str(i) for i in l if len(str(i))==1]
    res = [k for k , v in dic.items() if v in st]
    
    return list(reversed(res))

if __name__ == "__main__":
    print(words_digits_backwards(l1))
    print(words_digits_backwards(l2))