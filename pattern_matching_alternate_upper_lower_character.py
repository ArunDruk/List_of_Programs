''' Check if the alternate characters are in upper and lower case, if YES return TRUE else False'''
import re
mystr = "AaZzBn"

out = re.search(r'([A-Z][a-z])+',mystr)
print(out.group())
if out.group() == mystr:
    print(True)
else:
    print(False)