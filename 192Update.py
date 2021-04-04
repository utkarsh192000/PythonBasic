#  this is used to update the dictionary of with key value pair




stu={
    101:"Rahul",
    102:"raj",
    103:"Sonam",
}

print(stu)
print(id(stu))

stu.update({102:"suresh"})
print(stu)
print(id(stu))

vals={
    "name":"Sushma",
    108:"Ramesh",
    "course":"English"
}
stu.update(vals)
print(stu)