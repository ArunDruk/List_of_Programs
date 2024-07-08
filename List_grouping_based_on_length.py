from collections import defaultdict
d = defaultdict(list)
lis = ['sight', 'first', 'foo', 'love', 'at', 'was', 'at', 'It']
for x in L:
  d[len(x)].append(x)
l1=list(d.values())
print(l1)