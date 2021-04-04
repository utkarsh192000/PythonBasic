#  if the name of global and local variable is same , then keyword global keyword is used to differentiate

a=50
def show():
    a=10
    print(a)  # since the name of global and local is same then local is prefereed

show()



i=0
def show():
    global i  # now specifically global variable would be used
    i=i+1
    print(i)  # since the name of global and local is same then local is prefereed

show()
print(i)