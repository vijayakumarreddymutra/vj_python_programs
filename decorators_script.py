'''
def my_in(j):
    def my_de(func):
        def my_wrap(*a,**b):
            for i in range(j):
                func(*a,**b)
        return my_wrap
    return my_de


@my_in(5)
def my_fun():
	print("hi")

my_fun()

#########################################################################


def my_fun():
	print("hi")

for _ in range(3):
    my_fun()




    for _ in range(3):
        print("hi")
        
        
    for i in range(3):
    print("hi")

'''

def my_in(j):
    def my_de(func):
        def my_wrap(*a,**b):
            import time
            start_time = time.time()
            print(start_time)
            for i in range(j):
                func(*a,**b)
            end_time = time.time() - start_time
            print(end_time)
        return my_wrap
    return my_de


@my_in(500000)
def my_fun():
	pass

my_fun()

print("*" * 30)
def my_fun1():
	pass

import time
start_time = time.time()
for _ in range(500000):
    my_fun1()
end_time = time.time() - start_time
print(end_time)














