
# list[start:end-1:stepsize]


a=[100,102,103,104,105,106,107,108,109,110]
print(a)
print(len(a))

print()

print(a[2:5])   # it will print from index 1 to 4
print(a[0:7])
print(a[:len(a)])
print(a[0:6])
print(a[2:])  # from 2 to last
print(a[-1:])  # just print last
print(a[-4:-3])  # -4-(-3)=-1 means last 4 element and then 1st element in that
print(a[0:5:1])   # 0,1,2,3,4
print(a[0:5:2])  # 0,2,4,
print(a[0:])
print(a[::-1])  # reverse the list
print(a[len(a):1:-1])  #9,8,7,6,5,4,3,2 index
print(a[8:3:-2])  # 8,6,4

