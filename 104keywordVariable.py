
#  instead of indexing it is accessed using key value pair

def add(x,*num):
    z=x+num["a"]+num["b"]+num["c"]
    print(z)

add(4,a=2,b=6,c=8)