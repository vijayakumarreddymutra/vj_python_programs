#all insta code

#unpacking list or tuple or set using * operator before

#a = {1:2,3:4}
#print(*a)

'''
#merge two dicts
a={"virat":10}
b = {"rohit":20}

c = {**a,**b}
d = a | b

print(c,d)
'''

'''
#to get the size of a list we can use sys.getsizeof()
a = (i for i in range(10000000))
import sys
res = sys.getsizeof(a)/10**6
print(res)

#we can use Lock.acquire() and Lock.release()
'''
'''
class MyClass:

    def __new__(cls,*args,**kwargs):
        print("before object")
        print(cls)
        #return super().__new__(cls)
        
    def __init__(self):
        print(self)
        print("After object")

obj = MyClass()
'''


class MyClass:
    __slots__ = ["a","b"]
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
ab = MyClass(1,2)
print(id(ab.__dict__))
print(id(ab))