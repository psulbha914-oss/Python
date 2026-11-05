# Q1.WAF to print the length of a list.(list is the parameters)

cities=["delhi","pune","mumbai","noida","gurgaon","chennai"]
heroes=["thor","ironman","captain","shaktiman"]

def print_len(list):
    print(len(list))

print_len(cities)  
print_len(heroes)  



# WAF to print the elements of a list in a single line.(list is the parameters)

def print_list(list):
    for item in list:
        print(item,end=" ")

print_list(heroes) 


# WAF to find the factorial of n.(n is the parameter.)   # n factorial = n!
def cal_fact(n):
    fact=1
    for i in range(1,n+1):
        fact *=i
    print(fact)    

cal_fact(5)    


# WAF to cinvert USD to INR

def converter(usd_val):
    inr_val=usd_val*83
    print(usd_val,"USD =",inr_val,"INR")

converter(2)    

# Write a recursive function to print all elements in a list. Hint: use list & index as parameters.

def print_list(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)
fruits=["mango","litchi","apple","banana"] 
print(list[fruits])   


# file que solving..

# 1. Create a new file"practice.txt"using pythn. Add th following data in it.

# Hi everyone
# we are learning file i/o
# Using java.
# i like programming in java.

with open("practice.txt","w") as f:
    f.write("Hi everyone\nwe are learning file i/o\n")
    f.write("Using java.\ni like programming in java.")



# WAF that replaces all occurences of"Java" with "python" in above file.
with open("practice.txt","r") as f:
    data=f.read()
new_data=data.replace("java","python")
print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)

# Search if the world "learning" exicts in the file or not.
word="xlearning"
with open("practice.txt","r")as f:
    data=f.read()
    if(data.find(word) !=-1):
        print("found")
    else:
        print("not found")
   
   
















