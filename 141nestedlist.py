a=[10,20,30,40,[50,60]]

print(a)
print()
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print()
print(a[4][0])
print(a[4][1])
print()
# print(a[1][0]) # this would give error as the the index is not subscriptable

a[4][0]=55
a[2]=46
print(a)

print()
#  Nested list in form matrix or 2-d array

a=[[10,20,30],
[40,50,60]] # it is like 2*3 matrix, indexing would be same like matrix or simple list


print(a)
print()
print(a[0][0])
print(a[0][1])
print(a[0][2])
print(a[1][0])
print(a[1][1])
print(a[1][2])