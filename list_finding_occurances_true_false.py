# L=[1,1,1,2,2,3]
L=[1,1,4,4]
d={}
for i in L:
   d[i]=L.count(i)

L1=list(d.values())
L2=set(list(d.values()))

if len(L1) == len(L2):
    print(True)
else:
    print(False)