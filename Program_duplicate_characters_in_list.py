''' Program to print duplicate characters in the list'''
l1=['india','is', 'my', 'country']
# output = ['i','n','y']
s1 = "".join(l1)
print(s1)
l2=[]

''' to get duplicate characters'''
for j in s1:
    if s1.count(j) > 1 and j not in l2:
        l2.append(j)
print(l2)
print(*l2)