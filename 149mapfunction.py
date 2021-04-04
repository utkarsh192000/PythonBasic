a=[10,20,30,40,50]

def inc(n):
    return n+2

result=map(inc,a)
# result=map(lambda n:n+2,a)   lambda function could also be written inplace  of function
print(result)
print(type(result))  # it is map object

print()
print(list(result))  # typecast that object in list




#  Example

a1=[10,20,30,40,50]
a2=[1,2,3,4,5]

result=map(lambda n,m:n+m,a1,a2)
print(list(result))