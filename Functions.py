
# Functions.
 # Block of statement thet perform a specific task.
# function defination

# with parameter
def calc_sum(a,b):     # a and b = parameters
    return a+b

sum=calc_sum(1,2)     # calc_sum=function call.
                       # 1,2= Argument
print(sum)

# without parameter
def print_hello():
    print("hello")

print_hello()    


# average of 3 numbers.
def calc_avg(a,b,c):
    sum=a+b+c
    avg=sum/3
    print(avg)
    return avg

calc_avg(1,2,3) 


# type of function in python

# 1.Built-in functions
      # print()
      #len()
      #type()
      #range()
    
# 2.user defined functions

# default parameters
# assigning a default value to parameter,which is used whenno argument is passed.
def cal_prod(a=4,b=2):
    print(a*b)
    return a*b
cal_prod()






