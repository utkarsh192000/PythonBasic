#  tuple are immutable , we cannot change a particular elemnt,unlike List
# 

a=(10,20,30,21.6,-50,"GeekyShows")

print(a)

# a[3]=45    this would give an error as tuples are immutable, Type error

#  But through logic they can be modified after concat and then adding

a=(10,20,30,21.6,-50,"GeekyShows")
tup2=a(0:3)

#  we can slice and then concat 