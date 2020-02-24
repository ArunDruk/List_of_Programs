L=[4,1,7,3,2]

for i in range(len(L)+1):
    # print(i)
    for j in range(i+1,len(L)):
        # print(j)
        if(L[i]>L[j]):
            # print(L[i],L[j])
            # temp=L[i]
            # L[i]=L[j]
            # L[j]=temp
            L[i],L[j]=L[j],L[i]
            # print(L[i], L[j])
            print(L)

print(L)
