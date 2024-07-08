'''
A Closure is an inner function that remembers and has access to the variables
in the local scope which is created even though it doesn't have access to outer function
'''
####################################################################################################
# def outer_func(msg):
#     text=msg
#     def inner_func():
#         print(text)
#     return inner_func


# hello_var=outer_func("Hello")
# hi_var=outer_func("Hi")

# hello_var()
# hi_var()
####################################################################################################
import logging
logging.basicConfig(filename='example.log',level=logging.INFO)
def outer_func(func1):
    def wrap_func(*args):
        print(f"this log from: {func1.__name__}")
        logging.info('Running "{}" with arguments {}'.format(func1.__name__,args))
        return func1(*args)
    return wrap_func

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

add_res=outer_func(add)
sub_res=outer_func(sub)

print(add_res.__name__) ## This is same as wrap_func
print(add_res(5,6))
print(sub_res(8,3))