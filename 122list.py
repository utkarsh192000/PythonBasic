a=[10,20,-23,21.3,"GeekyShows"]
print("id:" ,id(a))
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[-1])
print(a[-2])
print(a[-3])
print(a[-4])
print(a[-5])

#  Mutability of list
a[2]=30
print(a)
print("id: ",id(a))  # even after reassiging the address has not changed

print(id(a[0]))
print(id(a[1]))
print(id(a[2]))
print(id(a[3]))
print(id(a[4]))