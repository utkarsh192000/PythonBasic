#  THis method reurn the specified value 
#  if key is not found , it inserst this key value pair in dictionary


stu={
    101:"Rahul",
    102:"raj",
    103:"Sonam",
}

returned_value=stu.setdefault(102,"Python")
print(returned_value)

stu.setdefault(107,"GeekyShws")
print(stu)   # since 107 is not present therefor this key value pair would be inserted inside the dictionary
