a=[10,20,-50,21.3,"geekyShows"]
#  it will always add at the end of the list

print("Before")
print()
for i in a:
    print(i)

print()
a.append(35)

print("After")
print()
for i in a:
    print(i)
