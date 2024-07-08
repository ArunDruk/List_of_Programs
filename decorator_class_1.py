class deco_class:
    def __init__(self,original_func):
        self.original_func=original_func
    
    def __call__(self, *args, **kwds):
        print(f"call method executed this before: {self.original_func.__name__}")
        return self.original_func(*args,**kwds)


@deco_class
def display():
    print("This is a display func")

print(display)
display()  ##  This is actually calling the __call__ method inside the class deco_class

