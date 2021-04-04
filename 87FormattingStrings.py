

# print("{}".format(10))  # do not give any space between {}
# print("{} {}".format(10,20))
# print("{0} {1}".format(10,20))   # we havent yet used format specifier
# print("{1} {0}".format(10,20))
# print("{num1} {num2}".format(num1=10,num2=20))
# print("{num2} {num1}".format(num1=10,num2=20))




# print("{}".format(10.56))  # do not give any space between {}
# print("{} {}".format(10.56,20.42))  # without considered as string any format specifier it is 
# print("{0} {1}".format(10.56,20.42))
# print("{1} {0}".format(10.56,20.42))
# print("{num1} {num2}".format(num1=10.56,num2=20.42))
# print("{num2} {num1}".format(num1=10.56,num2=20.42))


# print("{}".format("Geeky"))  # do not give any space between {}
# print("{} {}".format("Geeeky","shows"))  # without considered as string any format specifier it is 
# print("My name is {1} {0}".format("Geeky","shows"))
# print("{str2} {str1}".format(str1="Geeky",str2="shows"))




# print("{}".format(10))  # printed as string
# print("{:d}".format(10))  # printed as integer
# print("{0:d}".format(10))  # printed as integer along with index


#  FORMAT Specifier


# print("{num}".format(num=15))
# print("{num:5d}".format(num=15))
# print("{num:05d}".format(num=15))
# print("{num:+5d}".format(num=15))
# print("{num:<5d}".format(num=15))
# print("{num:*<5d}".format(num=15))
# print("{num:*>5d}".format(num=15))
# print("{num:^5d}".format(num=15))
# print("{num:*^5d}".format(num=15))


# print("{num}".format(num=15.45))
# print("{num:f}".format(num=15.45))
# print("{num:8.3f}".format(num=15.45))
# print("{num:<8.3f}".format(num=15.45))

# print("{:s}".format("Geeky"))
# print("{:8s}".format("Geeky"))
# print("{:<8s}".format("Geeky"))
# print("{:>8s}".format("Geeky"))
# print("{:^8s}".format("Geeky"))


name="Rahul"
age=20
print("My name is {} and my age is {} ".format(name,age))


print()

a=50
b=3
print("{:.2%}".format(a/b))

print()

data={'rahul':2000,'sonam':3000}
# print("{[rahul]:d} {[sonam]:d}".format(data))