#  generator oobject
#  yield is basically a type of return 
#  next is used to see the next elemnt of generator object


# def disp(a,b):
#     yield a
#     yield b

# result=disp(10,20)
# print(result)
# print(type(result))
# print(list(result))

# print(next(result))
# print(next(result))


#  Example 2

def show(a,b):
    
    while(a<=b):
        yield a 
        a+=1

result=show(1,5)
print(result)
print(type(result))

print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))


