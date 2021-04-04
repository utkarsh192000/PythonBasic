#  items return a object that contain key value pair
#  stored as tuple of object


stu={
    101:"Rahul",
    102:"raj",
    103:"Sonam",
}

it=stu.items()
print(it)
print(type(it))    # it is like dict object
lst=list(it)
print(lst)   # it is list of tuple

print(lst[0])
print(lst[0][0])
print(lst[0][1])
print(lst[1])
print(lst[2])