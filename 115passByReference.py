#  in python there is no paas by reference
#  instead there is pass by object reference

def val(x):
    print(x,id(x))
    x=15
    print(x,id(x))

x=10
val(x)
print(x,id(x))

#  This happend because integer are immutable and new object is created

#  for list this would not happen because they are mutable 

def val(lst):
    print(lst,id(lst))
    lst.append(4)
    print(lst,id(lst))

lst=[1,2,3]
print(lst,id(lst))
val(lst)
print(lst,id(lst))



#  in simple words if the object is modified , then the modified version wll be accessible outsid ethe func only if it is mutable


# Exmaple 

def val(lst1):
    print(lst1,id(lst1))
    lst1=[10,20,30]
    print(lst1,id(lst1))

lst1=[1,2,3]
print(lst1,id(lst1))
val(lst1)
print(lst1,id(lst1))

#  in thiscase both last are differnt and one inside the function is only accessible inside func and another ouside the func

