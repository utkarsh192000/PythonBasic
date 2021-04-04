#  function is automatically not called
def disp():
    name="Geekyshows"
    print(name)

disp()
disp()
disp()


def add():
    x=10
    y=20
    print(x+y)

def sub():
    x=50
    y=30
    print(x-y)

add()
sub()


def calc():
    add()
    sub()

print()

#  Defining a function without argument

def add1 ():
    x=10
    y=20
    c=x+y
    print(c)

add()


#  Function with argument

def addm(y):
    x=10
    c=x+y
    print(c)

addm(10)   # this is calling of function with argument


