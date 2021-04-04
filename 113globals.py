
a=50
def show():
    a=10
    print(a)
    x=globals()['a']
    print(x)
    x=40
    print(x)  # actually x is modified not global variable

show()

print(a)