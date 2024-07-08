a=12300
rev_num =0

print("Given num is ", a)

while (a):
    l = a % 10
    rev_num = rev_num * 10 + l
    a = a // 10


print("The reverse of the num is ", rev_num)