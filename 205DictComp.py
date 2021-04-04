

dict1={}

for n in range(10):
    dict1[n]=n*2
print(dict1)


dict2={n:n*2 for n in range(10)}
print(dict2)


dict3={n:n*2 for n in range(10) if (n%2==0)}
print(dict3)


dict4={n:(n*2 if (n%2==0) else "invalid") for n in range(10) }
print(dict4)