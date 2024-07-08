'''
Fist class functions means it takes function as a argument to another function, we can return a function
and also assign function to a variable and call that variable just like a function call.
'''

####################################################################################################
# def square(x):
#     return x*x

# # f=square
# # print(f(4))


# def mymap(func1,args):
#     res=[]
#     for i in args:
#         res.append(func1(i))
#     return res

# squares=mymap(square,[2,4,6,5,9])

# print(squares)
####################################################################################################
# def logger(msg):
#     def inner():
#         print(f'Log : {msg}')
#     return inner

# res=logger("Hi")
# res()

####################################################################################################
def head_tag(tag):
    def head2(msg):
        print(f"<{tag}> : {msg}")
        
    return head2

a1=head_tag('h1')  ## Now here a1 is same as head2, it's a function.
a1("this is from a1 tag") # calling the function head2 and passing the msg argument
a1('from a2 tag')

