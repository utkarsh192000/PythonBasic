#  dictionary inside dictionar
# to access the inside key of nested dict, go catch the key , then go inside and catch another key, then you will get its value

a={
    1:{},
    2:{},
    3:{}
}
print(a)

b={
    "course":"Python",
    "Fees":15000,
    1:{"course":"Javascript","fees":10000},
}

print(b)


print()

print(b["course"])
print(b[1]["course"])
print(b[1]["fees"])
print(b["Fees"])
print(b[1])

b[1]["course"]="MachineLearning"   # dict is modified
print(b)



#  Tod delete  use command del

del b[1]["course"]

print(b)

a["Duration"]=10
print(a)
a[1]["Time"]=20
print(a)