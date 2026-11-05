# I/O = input and output
# python can be used to perform operations on a file. (read&write data)

# types of all files
# 1. Text files: .txt,.docx,.log etc      # Character Files only
# 2. Binary files:.mp4,.mov,.png,.jpeg etc.     # Video files only
# RAM=Volatile(Not permentaly store data.)
# /n = next line character.
# Open a file.
# Truncate = file data delete.
# No Truncate = no file data delete.

# "r"=read.
# "w" = write.
# r+ = over write (reading and writing).( pointer starting) no Truncate
# w+ = reading and writing. (Truncate)
# a+ = read and append ( jab append to pointer end) no truncate.





f=open("First_program.py","r")
data=f.read()
print(data)
print(type(data))
line1=f.readline()
print(line1)
f.close()


# Writing to a file
f=open("First_program.py","a")
f.write("My name is sulbha kachare")
f.close



# With syntax
# with = Atomatically close a file.

with open("sets.py","r") as f:
    data=f.read()
    print(data)



# Deleting a file..
# 
# using the od module.
# Module (like a code library)is a file writeen by another programmer that generally has a functions we can use. 
# os = operating system

import os
os.remove("")









 
