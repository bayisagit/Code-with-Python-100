import math
def cal(area,cover):
    numof=math.ceil(area/cover)
    print(f"you will need {numof} cans of paint!")
height=float(input("what is the height of your wall:"))
width=float(input("what is the width of your wall:"))
cover=int(input("what is the cover of your wall:"))
area=height*width
cal(area,cover)
