# A valid filename should end in .txt, .exe, .jpg, .png, or .dll, and should 
#have at least three digits, no additional periods. Write a Python program to create a list of True/False that determine whether candidate filename is valid or not.
# Input:
# l1 = ['abc.txt', 'windows.dll', 'tiger.png', 'rose.jpg', 'test.py', 'win32.exe']
# Output:
# ['Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes']
# Input:
# l2 = ['.txt', 'windows.exe', 'tiger.jpeg', 'rose.c', 'test.java']
# Output:
# ['No', 'Yes', 'No', 'No', 'No']
def valid_filename(l):
    res = []
    for i in l:
        if i[-4] != ".":
            res.append("No")
        c = i.count(".")
        if c != 1 or  0 == len(i[:-4]):
            res.append("No")
        elif i.endswith(".txt") or i.endswith(".exe") or i.endswith(".jpg") or i.endswith(".png") or i.endswith(".dll"):
            res.append("Yes")
        elif i[:-4].isdigit() and len(i[:-4]) > 3:
            res.append("Yes")
    return res

if __name__ == "__main__":
    l1 = ['abc.txt', 'windows.dll', 'tiger.png', 'rose.jpg', 'test.py', 'win32.exe']
    l2 = ['.txt', 'windows.exe', 'tiger.jpeg', 'rose.c', 'test.java']
    print(valid_filename(l1))
    print(valid_filename(l2))
