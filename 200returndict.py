def show(d):
    print(d)
    print(type(d))
    for k in d:
        print(k,d[k])
    return d

dc={
    101:"Rahul",
    102:"Raj",
    103:"Sonam",
}

d1=show(dc)
print(d1)
print(type(d1))