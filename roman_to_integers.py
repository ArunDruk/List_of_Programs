def value(val):
    if val.upper() == 'I':
        return 1
    elif val.upper() == 'X':
        return 10
    elif val.upper() == 'V':
        return 5

# IX
def romanTointerger(s):
    res=0
    i=0
    while (i<len(s)):
        s1=value(s[i])
        if (i+1 <len(s)):
            s2=value(s[i+1])
            if (s1 >= s2):
                res=res+s1
                i=i+1
            else:
                res=res+s2-s1
                i=i+2
        else:
            res=res+s1
            i=i+1
    return res

s=input().strip()
out=romanTointerger(s)
print(out)