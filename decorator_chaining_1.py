from functools import wraps

def deco_func1(ori_func1):
    @wraps(ori_func1)
    def wrap_func1(*args,**kwargs):
        print(f"this is from wrap_func1: {ori_func1.__name__}")
        return ori_func1(*args,**kwargs)
    return wrap_func1

def deco_func2(ori_func2):
    # @wraps(ori_func2)
    def wrap_func2(*args,**kwargs):
        print(f"this is from wrap_func2: {ori_func2.__name__}")
        return ori_func2(*args,**kwargs)
    return wrap_func2

@deco_func1
@deco_func2
def display():
    print("This is a display func") # deco_func1(deco_func2(display))

display() 

dis=deco_func2(display)
print(dis.__name__)  # # To preseve the original information of the function, we use func tools
# # from functools import wraps
# print(dis)