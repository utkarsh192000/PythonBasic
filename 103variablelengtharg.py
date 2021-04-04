#  no. of argument is not maintained

def add(x,*y):
    z=x+y[0]   # if there are more than 1 value , then any value at instant can be accessed using indexing, first value automatically goes to the first parameter
    print(z)

add(5,2,4)