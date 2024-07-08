l=[1,2,3,3,2,3,1,4,5,6]
l1_non_dup=[]
l2_dup=[]
for i in l:
    if i in l1_non_dup:
        l2_dup.append(i)
    else:
        l1_non_dup.append(i)
print(l2_dup)
print(l1_non_dup)
D={}
for i in l:
    v=l.count(i)
    D[i]=v
print(D)