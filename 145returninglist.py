

def show(l):
    print(l)
    print(type(l))
    for i in l:
        print(i)
    return l

lst=[1,2,3,4,5,6,"GeekyShows","Help"]
new_lst=show(lst)  # if you store something then it simply means that you have to return something that it can be stored
print(new_lst)
print(type(new_lst))