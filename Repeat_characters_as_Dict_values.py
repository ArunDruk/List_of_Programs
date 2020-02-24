def Chacrater_repeat_to_Dictionary(s):
    D={}

    for i in s:
        c=s.count(i)
        D[i]=c

    return D,type(D)

if __name__=="__main__":
    print(Chacrater_repeat_to_Dictionary("abkbad"))