L=[3,0,1,0,1,0,4]
k=[]

for i in range(len(L)+1):
  for j in range(i,len(L)):
    if L[i] == 0:
      L[i],L[j]=L[j],L[i]

print(L)