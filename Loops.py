# Loops are used to repeat instructions.

# while loop
# for loop

 # while loop .......
# count=1
# while count<=5:
#     print("hello")
#     count+=1

# i=1
# while i<=50:
#     print("sulu",i) 
#     i+=1  




# i=5
# while i>=1:
#     print(i) 
#     i-=1   

# print("loop ended")    



# Let's practice.

# print numbers from 1 to 100.
i=1
while i<=100:
    print(i)
    i+=1


# print numbers from 100 to 1
# i=100
# while i>=1:
#     print(i)
#     i-=1

# # print the multiplication table of a number n.
# i=1
# while i<=10:
#     print(3*i)
#     i+=1

# n=int(input("enter number:")) 
# i=1
# while i<=10:
#     print(n*1)  
#     i+=1


# print the elements of the following list using a loops.
# nums=[1,4,9,16,25,36,49,64,81,100]

# idx=0
# while idx<len(nums):
#     print(nums[idx])
#     idx+=1

# search for a number x in this tuple using loop.
#     
# nums=[1,4,9,16,25,36,49,64,81,100]
# x=36
# i=0

# while i <=len(nums):
#     if(nums[i]==x):
#         print("FOUND at idx")
#     else:
#         print("Finding..")    
#     i+=1    

# Break and countinue
# Break: used to terminate the loop when encountered.
# continue: terminates execution in the current iteration & continues execution of the loop with the next iteration.
i=0
while i<=5:
    if(i==3):
        i+=1
        continue
    print(i)
    i+=1
