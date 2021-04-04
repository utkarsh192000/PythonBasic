#  we can delete entire tuple but no a specific elment as they are immutable


a=(10,20,30,40,"Geeky")

# del a # this would delete whole tuple

# del a[1] this would error as tuples are immutable , no change in specific

#  WE can use slicing and concat 
# tup=a[0:3]    it would remove rest of the elemnt

s1=a[0:3]
s2=a[4:]
print(s1+s2)   # this may remove 3rd index elemnt
