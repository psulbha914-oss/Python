# set is the collection of the unordered items.
# Each element in the set must be unique&immutable (not cheangable).
# only uniqye value
# hashvalue=immutable


collection={1,2,3,4}
print(collection)
print(type(collection))


collection={1,2,2,2,"hello","world","world"}
print(collection)
print(len(collection))


# empty set created.
collection=set()
print(type(collection))


# set methods.

# set.add(el)  # adds an element
# set.remove(el)  #removes the element
# set.clear()  #emties the set
# set.pop() # removes  a random value
# set.union(set2) #combines both set values&returns new
# set.intersection(set2) #combines common values & returns new

# set is a mutable but set element are unmutable.
collection.add(1)
collection.add(2)
collection.add(2)
print(collection)

set1={1,2,3}
set2={2,3,4}
print(set1.union(set2))
print(set1.intersection(set2))


# let's practice
# store following word meanings in a python dictionary:

dic={
    "cat":"a small animal",
    "table": ["a piece of furniture","lists of facts and figures"]
}

print(dic)






 