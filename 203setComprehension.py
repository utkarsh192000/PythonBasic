#  same as list

set1={0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19}
new_set1=set()
for i in set1:
    new_set1.add(i+1)

print(new_set1)

#  same thing can be done with the help of set comprehension
setc={i+1 for i in range(20)}
print(setc)

setc2={i+1 for i in range(20) if i%2==0}  
#  0 
print(setc2)

setc3={i if i%2==0 else i*100 for i in range(20)}
print(setc3)
#  remember the ordercan be anything so dont panic