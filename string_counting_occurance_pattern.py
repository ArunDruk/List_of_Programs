print('Hello World')
Actual = "abbcccddddeeeee"
# Expected : a1b2c3d4e5
d = {}
count = 1
for i in Actual:
    v=Actual.count(i)
    d[i]=v

# for i in range(len(Actual)):
#     for j in range(i, len(Actual)):
#         if Actual[i] == Actual[j]:
#             count += 1
#
#         d[Actual[i]] = count
#     count = 1

s=""
for key, val in d.items():
    s=s+key+str(val)
print("Input String: ",Actual)
print(d)
print(s)