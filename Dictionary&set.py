# Dictionaries are used to store data values in key:values pairs
# they are unordered,mutable(changeable)&don't allow duplicate keys.

info={
    "key" :"value",
    "name" :"sulbha",
    "learning" :"coding",
    "age":35,
    "is_adult":True,
    "marks":96.4

} 
print(info)

# nested dictionaries

students={
    "name":"sulbha",
    "subject":{
        "math":87,
        "phy":54,
        "eng":46
    }

}
print(students)
print(students["subject"]["math"])


# Dictionaries methods.
# myDict.keys()  # returns all keys 
# myDict.values() # returns all values
# myDict.items() # returns all(key,val)pairs as tuples
# myDict.get() #returns the key according to value
# mtDict.update(new Dict) # inserts the specified items to the dictionary






