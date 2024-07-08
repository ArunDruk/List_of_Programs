
# Chaining of decorators : the lower ones get executed first then the higher ones

def deco_func(func1):
    def wrapper_func(*args,**kwargs):
        print(f"call method executed this before: {func1.__name__}")
        return func1(*args,**kwargs) ## This actually calling the display function
    return wrapper_func


@deco_func
def display():
    print("This is a display func")

print(display.__name__)  ## This actually calling the wrapper_func
display()

# deco_func(display) # decorator calling