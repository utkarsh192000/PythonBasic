#  return single value

def add(y):
    x=10
    c=x+y
    return c

sum1=add(20)
print(sum1)


#  return multiple value


def add1(y):
    x=50
    c=x+y
    d=x-y
    return c,d

sum1,sub1=add1(20)
print(sum1,sub1)