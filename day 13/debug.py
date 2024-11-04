def mutate(alist):
    blist=[]
    for item in alist:
        neitem=item*2
        blist.append(neitem)
    print(blist)
can=[1,2,3,5,8,13]
mutate(can)