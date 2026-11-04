# for loops are used to sequential traversal.for traversing list,string,tuples etc.

list=[1,2,3]
for el in list:
    print(el)

list=("sulbhakachare")    
for el in list:
    print(el)

# for loop with else
#     
str="apnacollage"
for char in str:
    print(char)
else:
    print("END")   

# let's practice
# using for
# print the elements of the following list using a loop.

nums=[1,4,9,16,25,36,49,64,81,100]
for el in nums:
    print(el)


# search for a number x in this tuple using loop.
nums=[1,4,9,16,25,36,49,64,81,100,49]
x=49
idx=0
for el in nums:
    if(el==x):
        print("number found at idx",idx)
    idx+=1  

     
