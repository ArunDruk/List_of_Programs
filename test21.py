
# n=5
# for i in range(n):
#     # for j in range(1,n-1):
#     print(" ",i*'*')

def pattern(n):
#
    k = 2 * n - 2   # This gives the initial spacing distance here 8 whitespaces.
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print("*", end=" ")
        print("\r")
#
#
pattern(5)
