# Write a Python program to convert GPAs to letter grades according to the following table:
# GPAs	Grades
# 4.0:	A+
# 3.7:	A
# 3.4:	A-
# 3.0:	B+
# 2.7:	B
# 2.4:	B-
# 2.0:	C+
# 1.7:	C
# 1.4:	C-
# below:	F
# Input:
# l1 = [4.0, 3.5, 3.8]
# Output:
# ['A+', 'A-', 'A']
# Input:
# l2 = [5.0, 4.7, 3.4, 3.0, 2.7, 2.4, 2.0, 1.7, 1.4, 0.0]
# Output:
# ['A+', 'A+', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'F']

def grades(l):
    res = []
    for i in l:
        if i >= 4.0 and i<=5.0:
            res.append("A+")
        elif i>= 3.7 and i<=3.9:
            res.append("A")
        elif i>=3.4 and i<=3.6:
            res.append("A-")
        elif i>=3.0 and i<=3.3:
            res.append("B+")
        elif i>=2.7 and i<=2.9:
            res.append("B")
        elif i>=2.4 and i<=2.6:
            res.append("B-")
        elif i>=2.0 and i<=2.3:
            res.append("C+")
        elif i>=1.7 and i<=1.9:
            res.append("C")
        elif i>=1.4 and i<=1.6:
            res.append("C-")
        elif i<=1.3:
            res.append("F")
    
    return res
if __name__ == "__main__":
    l1 = [4.0, 3.5, 3.8]
    l2 = [5.0, 4.7, 3.4, 3.0, 2.7, 2.4, 2.0, 1.7, 1.4, 0.0]
    print(grades(l1))
    print(grades(l2))