s= "String sWaping Case"
a=s.swapcase()
print(s)
# print(a)

import string
new_s=""
u=string.ascii_uppercase
for i in s:
    if i in u:
        new_s=new_s+i.lower()
    else:
        new_s=new_s+i.upper()

print(new_s)

