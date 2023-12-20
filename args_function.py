# def func1(*ar):
#     print(len(ar))
#     for i in ar:
#         print(i)
#
#
# func1("this",1,1.234)

def func2(**kwargs):
    print(type(kwargs))
    for k,v in kwargs.items():
        print(f"key {k} - value '{v}'")


func2(first='a',sec='b')