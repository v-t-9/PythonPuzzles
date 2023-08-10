# 5. Write a Python program to check the nth-1 string is a proper substring of
# the nth string in a given list of strings.
# Input: ['a', 'abb', 'sfs', 'oo', 'de', 'sfde']
# Output:
# True
# Input: ['a', 'abb', 'sfs', 'oo', 'ee', 'sfde']
# Output:
# False
# Input: ['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwrew']
# Output:
# False
# Input: ['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwsfsdfrew']
# Output:
# True

def substring(l):
    s1 = l[len(l)-1]
    s2 = l[len(l)-2]

    if s2 in s1:
        return True
    else:
        return False

if __name__ == "__main__":
    l1 = ['a', 'abb', 'sfs', 'oo', 'de', 'sfde']
    l2 = ['a', 'abb', 'sfs', 'oo', 'ee', 'sfde']
    l3 = ['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwrew']
    l4 = ['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwsfsdfrew']
    print(substring(l1))
    print(substring(l2))
    print(substring(l3))
    print(substring(l4))

