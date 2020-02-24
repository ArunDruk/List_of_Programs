####################################################################################################
#Method 1: Converting to a Set
# L=[1,2,3,4,3,4]
# L1=list(set(L))
# print(L1, type(L1))

####################################################################################################
# Method 2: Using logic, Checking the list if not present append it
# L=[1,2,3,4,3,4]
# L1=[]
# for i in L:
#     if i not in L1:
#         L1.append(i)
#
# print(L1)
####################################################################################################

# Method 3: Using List comprehension : writing the logic in a single line approach using []
# L=[1,2,3,4,3,4,7,7]
# L1=[]
#
# [L1.append(i) for i in L if i not in L1]
# print(L1)

####################################################################################################

#Method 4: using dictionary
L=[1,2,3,4,3,4,7,7]
L1=list(dict.fromkeys(L))
print(L1)
