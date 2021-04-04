#  just a way of writing a shoe=rt code using loops

# synatax
# lst=[expression for item in iterable_object if_statement]


lst1=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,]
new_lst1=[]
for i in lst1:
    new_lst1.append(i+1)
print(new_lst1)  # adds 1 to each element

#  same code using list comprehension

lst2=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,]
new_lst2=[i+1 for i in lst2 ]
print(new_lst2)



# list compreshension complex code using if 

lst3=[]
for i in range(20):
    if(i%2==0):
        lst3.append(i)
print(lst3)

lst4=[i for i in range(20) if (i%2==0)]
print(lst4)

lst5=[i for i in range(20) if (i%2==0) if(i%3==0)]
print(lst5)


#  LS with if else

lst5=[i if (i%2==0) else "Invalid" for i in range(20) ]
print(lst5)


#  same code with normla if else

lst6=[]
for i in range(20):
    if(i%2==0):
        lst6.append(i)
    else:
        lst6.append("Invalid")
print(lst6)
