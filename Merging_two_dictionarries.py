####################################################################################################
# Merging two dictionaries D1 and D2 and producing Dictionary D3.
####################################################################################################

# D1={1:'a',2:'b'}
# D2={3:33,4:("aa","bb")}
# D3={**D1,**D2}
# print(type(D3),D3)

####################################################################################################

dic1={'num1':20,'num2':30,'num4':10}
dic2={'num1':40,'num3':60}
dic3={}

dic3.update(dic2)
for i in dic1.keys():
    if i in dic2.keys():
        dic3[i]=dic1[i]+dic2[i]
    else:
        dic3[i]=dic1[i]
print(dic3)

