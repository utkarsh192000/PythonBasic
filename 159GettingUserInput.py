#  direction insertion is not allowed

#  take list as input and then typecast into tuple

a=[]
for i in range(int(input())):
    a.append(int(input()))
print(a)
print(type(a))
c=tuple(a)
print(c)
print(type(c))