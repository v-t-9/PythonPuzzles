# Write a Python program to test a list of one hundred integers between 0 and 999, 
# which all differ by ten from one another. Return True otherwise False.
# Input:
l1 = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990]
# Output:
# True
# Input:
l2 = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500, 520, 540, 560, 580, 600, 620, 640, 660, 680, 700, 720, 740, 760, 780, 800, 820, 840, 860, 880, 900, 920, 940, 960, 980]
# Output:
# False

def differentint100(l):
    if len(l) == 100:

        for i in range(0, len(l)):
            if type(l[i]) == int:
                if l[i] - l[i+1] == -10:
                    return print(True)
                else: 
                    return print(False)
            else: 
                return print(False)
        for i in range(0,l[::-1]):
            if type(l[i]) == int:
                if i - (i+1) == 10:
                    return print(True)
                else: 
                    return print(False)
            else: 
                return print(False)
    else:
        return print(False)    
    
differentint100(l1)
differentint100(l2)
