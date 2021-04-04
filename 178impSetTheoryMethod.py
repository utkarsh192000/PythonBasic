# Union,intersection,


a={"Rahul","Raj","Sonam","Rani"}
b={"Sumeet","Rahul","Rani","Python","Java"}

print(a)
print(b)

ism=a.intersection(b)   # which are common in both
print(ism)

uni=a.union(b)
print(uni)

d=a.difference(b)
print(d)

d1=b.difference(a)
print(d1)

i=a.issubset(b)
print(i)

j=a.issuperset(b)
print(j)