# import re
# l=["This is my mail ID arundruk@gmail.com", "my ericsson ID is arun.s.kumar@ericsson.com"]
# mail_ids=[]
# j=len(l)
#
# for i in range(0,j):
#     mail_id=re.search(r'([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\.\-]+)\.[a-zA-Z0-9]{2,8}$',l[i])
#     mail_ids.append(mail_id.group())
# #^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$
#
# print(mail_ids)

count=0
for i in range(1,20):
    if("1" in i):
        count+=1

print(count)
