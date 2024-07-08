l=['a',1,2,'b','c',3,'k',4,5]
l1=[]
for i in l:
    k=type(i)
    c=str(k).find('int')
    if c>0:
         l1.append(i)

print(l1)