#  this are varible which are available for anything written down it
#  if the name of function and gloabal variable is same then . local variable is given preference

a=50
def show():
    x=10
    print(x)
    print(a)   # a can be used anywhere since it is a global variable

show()
print(a)
# print(x) # this would give error as it is local variable