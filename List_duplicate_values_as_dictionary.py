L=['a','b','b','a','b','c']
L1=list(set(L))
print(L1)
D={}
#count=1
# for i in L1:
#     count=0
#     for i in L:
#       count+=1
#       D[i]=count

for i in L1:
    k=L.count(i)
    D[i]=k
print(D,type(D))

# L3=[1,2,3,4]
# del L3[1]  # Deletes the element of a List with respect to index.
# print(L3)