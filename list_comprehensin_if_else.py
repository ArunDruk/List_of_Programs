# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#
# l=[i for i in fruits if i.count('a') >0]
# # l=[i if i.count('a') >0 else None for i in fruits]
#
# print(l)

########### List comprehension using if-else condition
l=list(range(10))
print(l)
### Odd cube, even square
l1=[i*i if i%2 ==0 else i*i*i for i in l ]
print(l1)