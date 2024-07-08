# when one needs to use the class as it without any modification,
# the composition (Has-a relation) is recommended and when one needs to change the behavior of the method in another class,
# then inheritance (Is-a relation) is recommended.


class A:
    def __init__(self):
        print("Am from Class A")

    def m1(self):
        print("Am from m1 method")

class C:
    def __init__(self):
        print("Am from class C")
        obj=A()
        obj.m1()

c=C()

