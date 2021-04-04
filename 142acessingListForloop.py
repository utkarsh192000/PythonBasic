a=[10,20,30,[50,60]]
n=len(a)  # 4

for i in range(len(a)): # (0,3)  4 times
    if type(a[i]) is list:
        if len(a[i])>1:
            m=len(a[i])
            for j in range(m):
                print(i,j,a[i][j])
    else:
        print(i,a[i])


#  For matrix type of list ,without index

b=[[1,2,3],
[4,5,6]]
print(b)

for r in b: # b itself is list , or we can also use len(b)
    for c in r: # we are already inside a nested list , so it will run len of its time
        print(c)


print()
print()

#  with index
b1=[[1,2,3],
[4,5,6]]
print(b1)

n=len(b1)


for i in range(n): # b itself is list , or we can also use len(b)
    for j in range(len(b1[i])): # we are already inside a nested list , so it will run len of its time
        print(i,j,b1[i][j])