# Write a Python program to select a string from a given list of strings with the 
# most unique characters.
# Input:
l1 = ['cat', 'catatatatctsa', 'abcdefhijklmnop', '124259239185125', '', 'foo', 'unique']
# Output:
# abcdefhijklmnop
# Input:
l2 = ['Green', 'Red', 'Orange', 'Yellow', '', 'White']
# Output:
# Orange

def uniqueCharacters(l):
    un = []
    for i in range(len(l)):
        un.append(len(set(l[i])))
    m = max(un)

    for i in l:
        if len(i) == m:
            return i
        

if __name__ == "__main__":
    print(uniqueCharacters(l1))
    print(uniqueCharacters(l2))