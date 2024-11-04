row1=[" "," "," ",]
row2=[" "," "," ",]
row3=[" "," "," ",]
map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
pos=input("where do you want to put the treasure:")
hor=int(pos[0])
ver=int(pos[1])
map[hor-1][ver-1]="x"
print(f"{row1}\n{row2}\n{row3}")

