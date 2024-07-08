s = 'india'
# output = 'e', 's'
l1=[]
for i in s:
    if s.count(i) == 1:
        l1.append(i)

# print(l1)

l2 =["india", "is", "my", "country"]
l3 = [i for i in l2 if i.startswith('i')]
# print(l3)

Actual = "abbcccddddeeeee"
# Expected : a1b2c3d4e5
s1=""
for i in Actual:
    if i not in s1:
        s1=s1+i
s2=""
for i in s1:
    s2= s2+ i + str(Actual.count(i))
print(s2)