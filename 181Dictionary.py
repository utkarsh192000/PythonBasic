#  Unordered collection
# Mutable
# Key Value pair
# keys cant repeated ,it should be unique,they arecasesense 
# if same key value is overridden
# key should be immutable type , int,string,tuple
#  value can be accessed key in []

d={}
print(d)
print(type(d))

d1={
    101:"Rahul",
    102:"RAJ",
    103:"Sonam",
}
print(d1)
print()
print(d1[101])
print(d1[102])
print(d1[103])


d2={
    "Rahul":2000,
    "RAJ":1000,
    "Sonam":500,
}


print(d2)
print()
print(d2["Rahul"])
print(d2["RAJ"])
print(d2["Sonam"])
