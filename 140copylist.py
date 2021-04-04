#  both list are indepenndent of each other after copying
#  cloning a list using slice , boht are independent of each other

a=[10,20,30,40,50]
print(a)

b=a.copy()
print(b)

c=a[:]
print(c)

b[2]=25
c[2]=30

print(b)
print(c)
