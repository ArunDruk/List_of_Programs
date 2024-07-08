####################################################################################################
# def outer1(func1):
#     def wrap_func1():
#         print("from wrap1")
#         func1()
#         print("after wrap1")
#     return wrap_func1

# def outer2(func2):
#     def wrap_func2():
#         print("from wrap2")
#         func2()
#         print("after wrap2")
#     return wrap_func2

# @outer1
# @outer2
# def myfunc():
#     print("hello")

# # res=outer(func1)
# res=myfunc
# # print(res.__name__)
# res()
####################################################################################################
####################################################################################################
def outer1(func1):
    def wrap_func1():
        print("from wrap1")
        func1()
        print("after wrap1")
    return wrap_func1

def outer2(func2):
    def wrap_func2():
        print("from wrap2")
        func2()
        print("after wrap2")
    return wrap_func2

@outer1
@outer2
def myfunc():
    print("hello")

res=outer(func1)
res=myfunc
# print(res.__name__)
res()