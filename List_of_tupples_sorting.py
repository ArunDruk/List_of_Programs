tup=[("Love",2),("India",3),("I",1)]

lst = len(tup)
#for i in range(0, lst):
for i in range(lst+1):
    #for j in range(0, lst - i - 1):
    for j in range(lst-1):
        if (tup[j][1] > tup[j + 1][1]):
            # temp = tup[j]
            # tup[j] = tup[j + 1]
            # tup[j + 1] = temp
            tup[j],tup[j+1]=tup[j+1],tup[j]
print(tup)
