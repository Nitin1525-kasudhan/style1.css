#DICTIONARY & SETS
"""dict = {
    "name" : "nitin",
    "cgpa" : 8.2,
    "marks" : [12,23,56],
}
print(type(dict))"""

#null dict
#null_dict = {}
#print(null_dict)


#nested form (13:39)apna collage 
"""student = {
    "name" : "nitin kasaudhan", 
     "subjects" : {
            "phy":87,
            "chem":67,
            "maths":89
    }
}

#print (student)"""

#dict method (keys method)
"""student = {
    "name" : "nitin",
    "subjects" : {
        "phy" : 97,
        "chem" : 87,
        "maths": 76
    
    }
}
print(student.keys())"""

#2:value method 
"""student = {
    "name" : "nitin",
    "subjects" : {
        "phy" : 97,
        "chem" : 87,
        "maths": 76
    
    }
}
print(student.values())"""


# 3: items method 
"""student = {
    "name" : "nitin",
    "subjects" : {
        "phy" : 97,
        "chem" : 87,
        "maths": 76
    
    }
}
print(student.items())"""

#4: get method(key )
"""student = {
    "name" : "nitin",
    "subjects" : {
        "phy" : 97,
        "chem" : 87,
        "maths": 76
    
    }
}
print(student.get("name"))"""

#update method (newDict)
"""student = {
    "name" : "nitin",
    "subjects" : {
        "phy" : 97,
        "chem" : 87,
        "maths": 76
    
    }
}
student.update({"city": "gorakhpr"})
print(student)"""


#SETS IN PYTHON
"""nums = {1,2,3,4,5,6,7,4,5,3,1,3,5,6,9,7}
print(type(nums))
print(nums)"""


#empity sets
#empity = set()
#print(type(empity))


#sets method 
# 1: ADD method
"""collection = set()
collection.add(1)
collection.add(2)
collection.add(4)

print(collection)"""

#2:REMOVE method 
"""collection = set()
collection.add(1)
collection.add(2)
collection.add(4)


collection.remove(2)
print(collection)"""

# 3: clear method 

"""collection = set()
collection.add(1)
collection.add(2)
collection.add(4)


collection.clear()
print(len(collection))"""

#4: POP value 

#collection = {"hi", "hello", "apna"}
#print(collection.pop())


# 5:union method
"""collection = {1,2,3,4,5}
collection = {1,2,3,4,5,6,7,8,9,0}
print(collection.union())"""

#6: intersection method 
"""collection1 = {1,2,3,4,5}
collection2 = {1,2,3,4,5,6,7,8,9,0}
print(collection1.intersection(collection2))"""


#PRASCTICE QUESTION
"""dict = {
    "cat" : "a small aniamal",
    "table" : ["a pice of furniture", "list of facts"]
}
print(dict)"""