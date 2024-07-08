
L=[3,0,1,0,5,7,0]
k=len(L)
L1=[]
for i in range(len(L)):
    if L[i]==0:
        L1.insert(k,L[i])
    else:
        L1.append(L[i])

print(L1)