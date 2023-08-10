#  Write a Python program to find all n-digit integers that start or end with 2.
# d1 = 1
# Output:
# [2]
# d2 = 2
# Output:
# [12, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 32, 42, 52, 62, 72, 82, 92]
# d3 = 3
# Output:
# [102, 112, 122, 132, 142, 152, 162, 172, 182, 192, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 302, 312, 322, 332, 342, 352, 362, 372, 382, 392, 402, 412, 422, 432, 442, 452, 462, 472, 482, 492, 502, 512, 522, 532, 542, 552, 562, 572, 582, 592, 602, 612, 622, 632, 642, 652, 662, 672, 682, 692, 702, 712, 722, 732, 742, 752, 762, 772, 782, 792, 802, 812, 822, 832, 842, 852, 862, 872, 882, 892, 902, 912, 922, 932, 942, 952, 962, 972, 982, 992]

def start_end_2(n):
    num = "1"
    a = 1
    c = []
    while a < n:
       num = num + "0"
       a += 1
    b = num + "0"
    for i in range(int(num),int(b)):
        c.append(i)
    res = [i for i in c if str(i).startswith("2") or str(i).endswith("2")]
    return res
    

if __name__ == "__main__":
    d1 = 1
    d2 = 2
    d3 = 3
    print(start_end_2(d1))
    print(start_end_2(d2))
    print(start_end_2(d3))
