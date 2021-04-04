# They are anonymous function
#  dont use def as keyword but lambda is used
#  can take any no. of argument but only 1 expression
#  can only contain expression , cant include statement

# def show(x):
#     print(x)

# show("Heelo")

show=lambda x:print(x)
show(5)

add=lambda x,y:x+y
print(add(5,3))



add_sub=lambda x,y:(x+y,x-y)   # it is returned in tuple form for multiple values
a,b=add_sub(10,6)
print(a,b)