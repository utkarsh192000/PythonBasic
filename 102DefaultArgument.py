#  if no argument is not given then default argument is used 

def show(name,age=27):
    print(name,age)

show(name="GeekyShows",age=62)  # in this case the value is given therefore the given age 62 will be used
show(name="GeekyShows")   # in this case since the value is not given therefore the default value of 27 will be used 

