# This program returns the first non repeating character in the string, suppose if there are no non-repeating character then this
# program returns a underscore '_'


def first_non_repeating_character(s):
    L=[]
    print(__name__)
    for i in s:
        L.append(i)

    L1=list(dict.fromkeys(L))
    for j in L1:
        #print(j)
        c=s.count(j)
        if c==1:
            return j
    # print(__name__)
    return '_'

if __name__=="__main__":
    print(first_non_repeating_character("abcbacy"))