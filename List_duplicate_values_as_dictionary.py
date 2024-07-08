L=['a','b','b','a','b','c']
L1=list(set(L))
# L1.sort()
print(L1)
D={}
#count=1
# for i in L1:
#     count=0
#     for i in L:
#       count+=1
#       D[i]=count

def counting(my_list,char):
    char_count=0
    for i in my_list:
        if i == char:
            char_count +=1
    return char_count

for i in L1:
    k=counting(L,i)
    # k=L.count(i)
    D[i]=k
print(D,type(D))

# L3=[1,2,3,4]
# del L3[1]  # Deletes the element of a List with respect to index.
# print(L3)