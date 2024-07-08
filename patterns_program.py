
''' program to print Triangle Pyramid'''
# n = 5
# for i in range(n): #rows
#     for j in range(i,n): # column to give the starting spaces
#         print("",end=" ")
#     for j in range(i+1): #column to print the stars
#         print('*',end = " ")
#     print()

''' program to print reverse pyramid '''
# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print('*', end = " ")
#     for j in range(i+1):
#         print("",end = "")
#     print()

# ''' program to print Hill pattern with stars'''
# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(' ', end= " ")
#     for j in range(i):
#         print("*",end =" ")
#     for j in range(i+1):
#         print("*", end=" ")
#     print()

''' program to print Hill pattern with numbers'''
n=5
for i in range(n):
    for j in range(i,n):
        print(' ', end= " ")
    if i%2 == 0:
        for j in range(i):
            print("1",end =" ")
    else:
        for j in range(i+1):
            print("2", end=" ")
    print()

''' Number pattern program'''

