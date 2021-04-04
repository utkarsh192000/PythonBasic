str1="Geeky"
print(str1)

str2='''please
help me'''
print(str2)

str3="I'll be back within the time "
print(str3)  # either use double quote inside single quote or single quote inside double quote

str4="Hello\nhow are you?? "
print(str4)

str4=r"Hello\nhow are you?? "  # r neglects the effect of escape sequence 
print(str4)
print(id(str4))

str5="shows"
str6="shows"
print("str5: ",id(str5))
print("str6: ",id(str6))  # they will have same memory address


str7="myshows"
print("str7: ",id(str7))
str7="Python"
print("str7: ",id(str7))

str1="Geekyshows"
print(str1)
print(str1[3])
print(str1[8])
print(str1[-1])
print(str1[-5])
print(str1[0])
