# ###########################################################################################################
#Below is the code to convert list to a dictionary.
# L=[1,2,3,4,3,4]
# D={L[i]:L[i+1] for i in range(0,len(L),2)}
# print(type(D), D)

# ###########################################################################################################
# Converting two lists having Key and Values to a dictionary using ZIP function.

# L1=[1,2,3,4]
# L2=['a','b','c','d']
# #D1=dict(zip(L1,L2)) # Method 1
# D1={k:v for (k,v) in zip(L1,L2)} # Method 2
# print(type(D1),D1)
# print(D1.keys())
# print(D1.values())
# ###########################################################################################################
# Each Key having multiple values, converting three lists to a dictionary, one list contains keys and two lists contains values.

# L1=[1,2,3,4]
# L2=['a','b','c','d']
# L3=["Apple","ball","cat","doll"]
# D1={k:(v1,v2) for (k,v1,v2) in zip(L1,L2,L3)}
# print(D1, type(D1))
# print(D1[1])