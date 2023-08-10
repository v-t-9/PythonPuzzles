# Write a Python program to find the largest number where commas 
# or periods are decimal points.
# Input: ['100', '102,1', '101.1']
# Output:
# 102.1
def largestNumberPoint(l):
    r = []
    for i in l:
        if "," in i:
            x = i.replace(",",".")
            r.append(x)
        else:
            r.append(i)
    return max(r)

if __name__ == "__main__":
    l1 = ['100', '102,1', '101.1']
    print(largestNumberPoint(l1))