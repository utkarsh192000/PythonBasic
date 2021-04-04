#  to find value of key
#  if no value is present it returns none


stu={
    101:"Rahul",
    102:"raj",
    103:"Sonam",
}

print(stu.get(101))
print(stu.get(108))
print(stu.get(108,"no value present" ))