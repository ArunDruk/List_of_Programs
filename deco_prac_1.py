####################################################################################################
# def outer(func):
#     def wrap_func():
#         print("############")
#         func()
#         print("%%%%%%%%%%%%%%%%%%%")
#     return wrap_func

# @outer
# def func1():
#     print("hello")

# # res=outer(func1)
# res=func1
# print(res.__name__)

# res()
####################################################################################################
####################################################################################################

class B:
    def method2(self):
        print("Class B, method1")

def outer(func):
    def wrap_func():
        print("############")
        func()
        print("%%%%%%%%%%%%%%%%%%%")
    return wrap_func

@outer
class A(B):
    def __init__(self):
        print("Am from Class A Constructor")
    
    def method1(self):
        print("Class A, Method1")

res=A
# print(res.__name__)
a=res()
# a.method2()

    
        