def my_main(j):    #j= 5 or 10
	def my_out(i):    #i = my_fun   #here function
		def wrap(*args,**kwargs):
			for _ in range(j):
				i(*args,**kwargs)
		return wrap
	return my_out



@my_main(5)
def my_fun():
	print("hi")


my_fun()

a = [1,2,3,4,5,6]
for i in a:
    a.remove(i)

print(a)   #[2,4,6]






