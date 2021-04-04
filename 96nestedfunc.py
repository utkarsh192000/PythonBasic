

#  1

def disp():
    def show():
        print("Show Function")
    print("Disp Function")
    show()
disp()

#  2

def disp():
    def show():
        return "Show Function"
    result=show()+" "+"Disp Function"
    return result
ans=disp()
print(ans)