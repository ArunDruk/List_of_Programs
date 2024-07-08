
# Chaining of decorators : the lower ones get executed first then the higher ones

def NavigationalDecoAPI():
    class Decowrapper:
        def __init__(self):
            print("This is from Constructor class Decowrapper")
        def __call__(self, *args, **kwds):
            print("This is from call method class Decowrapper")
            
    return Decowrapper

def elements(str_element):
    def outer_func(origin_func):
        def wrapper_func(*args,**kwargs):
            print(str_element+"  "+f"executed before Func: {origin_func.__name__}")
            origin_func(*args,**kwargs)
            print(str_element+"  "+f"executed after func: {origin_func.__name__}")
            return origin_func
        return wrapper_func
    return outer_func

@NavigationalDecoAPI()
@elements("Log")
class HomePageAPI:
    def __init__(self):
        print("This is a constructor func")

obj1=HomePageAPI()
print(HomePageAPI.__name__)  ## This actually calling the wrapper_func


# deco_func(display) # decorator calling