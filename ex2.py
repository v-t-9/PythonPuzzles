# 2. Write a Python program that accepts a list of integers and calculates the length and the 
# fifth element. Return true if the length of the list is 8 and the fifth element occurs thrice in the said list.

# Input: [19, 19, 15, 5, 5, 5, 1, 2]
# Output:
# True
# Input: [19, 15, 5, 7, 5, 5, 2]
# Output:
# False
# Input:  [11, 12, 14, 13, 14, 13, 15, 14]
# Output:
# True
# Input: [19, 15, 11, 7, 5, 6, 2]
# Output:
# False

def lengthAnd5Element(l):
    if len(l) == 8 and l.count(l[5])==3:
        return True
    else:
        return False
    
if __name__ == "__main__":
    l1 = [19, 19, 15, 5, 5, 5, 1, 2]
    l2 = [19, 15, 5, 7, 5, 5, 2]
    l3 = [11, 12, 14, 13, 14, 13, 15, 14]
    l4 =[19, 15, 11, 7, 5, 6, 2]
    print(lengthAnd5Element(l1))
    print(lengthAnd5Element(l2))
    print(lengthAnd5Element(l3))
    print(lengthAnd5Element(l4))




