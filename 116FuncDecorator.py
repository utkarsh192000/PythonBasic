#  decorator function accept function and returns the function


def decor(fun):
    def inner():
        print("Before enhancing")
        fun()
        print("After Enhancing")
    return inner


def num():
    print("We will use this function")
    print("and enhance this function")

result_fun=decor(num)
result_fun()
#  it is quite complex

#  basically decorator takes func , add feature and return it without interferring in actual function

print()
print()


def decor(fun):
    def inner():
        print("Before enhancing")
        fun()
        print("After Enhancing")
    return inner

@decor
def num():
    print("We will use this function")
    print("and enhance this function")

num()

#  the motive of decor is to enhance the feature of num

print()

# EXAMPLE 2


def decor (fun):
    def inner():
        a=fun()
        add=a+5
        return add
    return inner


def num():
    return 10

result_fun=decor(num)
print(result_fun())

