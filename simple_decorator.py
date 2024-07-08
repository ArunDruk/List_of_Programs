def greet_user(func):
    def inner_func():
        print("Good Morning!!")
        func()
    return inner_func

@greet_user
def func1():
    print("Hello User")

func1()