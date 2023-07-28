# Write a Python program to find an integer (n >= 0) with the given number of even and odd digits.
# Input:
# Number of even digits: 2 ,Number of odd digits: 3
e1 = 2
o1 = 3
# Output:
# 22333
# Input:
# Number of even digits: 4 ,Number of odd digits: 7
e2 = 4
o2 = 7
# Output:
# 22223333333

def digits(o,e):
    re = ""
    ro = ""
    for i in range(1,10):
        if i % 2 == 0:
            re = re + str(i)*e
            break
    for i in range(1,10):
        if i % 2 != 0:
            ro = ro + str(i)*o
            break
    return re + ro



if __name__ == "__main__":
    print(digits(o1,e1))
    print(digits(o2,e2))