L1=[]
string="This is Arun"
L=string.split(" ")
for i in L:
    j=i[::-1]
    L1.append(j)

s=" ".join(L1)
print(s)