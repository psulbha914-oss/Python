# When a function calls itself repeatedly.
# loos and recursion both are interrelated.
# 


# Recursive Function.
def show(n):
    if(n==0):   # Base case
        return
    print(n)
    show(n-1)

show(5)   



