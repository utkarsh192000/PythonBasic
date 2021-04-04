#  local variable is only accessible inside the function defined
#  if its is used outside then it will give errir

def add():
    x=10
    print(x)

add()

# print(x)    # thi would give error as x is local variable and scope of it is just inside the function
