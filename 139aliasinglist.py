#  aliasing simply means giving same name to diffrent list , any change in one will automatically affect the other


a=[10,20,30,40,50]
b=a
print(a)
print(b)

b[2]=4
print(a)
print(b)

# change in b is alos reflected in a 