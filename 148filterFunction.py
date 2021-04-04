# HIGHER order Function (fn inside fn)



#  filter always reurn elemnt which returns True


a=[10,50,60,80,90,5,45,65]

def high_marks(n):
    if n>60:
        return True



result=filter(high_marks,a)
# result=list(filter(lambda n:(n>=60),a))   we can also write lambda function rather than wriyting complex function
print(result)   # it is flter object not a list
print(list(result))

'''
for i in result:
    print(i)'''
print(type(result))