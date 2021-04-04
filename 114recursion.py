
#  function calling itself

import sys
print(sys.getrecursionlimit())
# sys.getrecursionlimit(4000)


i=0
def myfun():
    global i
    i=i+1
    print("My Func",i)
    myfun()

myfun()