#Dictionary and set
# info = {
#     "name" : "Naveen",
#     "age" : "20",
#     "studying" : "Btech",
#     "subjects" : ["python", "DSA"],
#     "learning" : "coding",
# }
# print(info)

#Nested dictionaries
# student = {
#     "name" : "Naveen",
#     "subjects" : { 
#         "phy" : 97,
#         "chem" : 98,
#         "math" : 95,
#     }
# }
# print(student["subjects"]

#Dictionary methods
#myDict.keys()
# student = {
#     "name" : "Naveen",
#    "subjects" : { 
#        "phy" : 97,
#         "chem" : 98,
#         "math" : 95,
#     }
# }
# print(student.keys())

#myDict.values()
# student = {
#     "name" : "Naveen",
#      "subjects" : { 
#          "phy" : 97,
#          "chem" : 98,
#          "math" : 95,
#      }
# }
# print(list(student.values()))

#myDict.items()
# student = {
#      "name" : "Naveen",
#    "subjects" : { 
#          "phy" : 97,
#         "chem" : 98,
#        "math" : 95,
#     }
# }
# print(student.items())

#myDict.get("keys")
# student = {
#       "name" : "Naveen",
#     "subjects" : { 
#           "phy" : 97,
#          "chem" : 98,
#         "math" : 95,
#      }
#  }
# print(student["name"])
# print("hi")
# print("welcome to")
# print("naveen")
# pr#int("i am student")
# print("coding")
      
#myDict.update(newDist)
# student = {
#        "name" : "Naveen",
#       "subjects" : { 
#           "phy" : 97,
#          "chem" : 98,
#         "math" : 95,
#              }
#  }
# new_dict = {"name": "Naveen", "age": 19}
# student.update(new_dict)
# student.update({"city" : "hyd"})
# print(student)

###set python
# collection = {1, 2, 3, 4, "hello", "world"}
# print(collection)
# print(len(collection))

# collection = set() 
# print(type(collection))

###set methods
#set.add(el)
# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add("Naveen")
# collection.add((1, 2, 3, 4))

# print(collection)  

#set.remove(el)
# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add("Naveen")
# collection.add((1, 2, 3, 4))

# print(len(collection))

#set.clear
# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add("Naveen")
# collection.add((1, 2, 3, 4))

# collection.clear()
# print(len(collection))

#set.pop() 
# collection = {"hello", "Naveen", "coding", "python", "apnacollege"}
# print(collection.pop())
# print(collection.pop())

#set.union(set2)
# set1 = {1, 2, 3} 
# set2 = {2, 3, 4}

# print(set1.union(set2))
# print(set1)
# print(set2)

#set.intersection(set2)
# set1 = {1, 2, 3}
# set2 = {2, 3, 4}

# print(set1.intersection(set2))

#################
#store following word meanings in a python dictionary;
# word_meanings = {
#     "cat" : "a small animal",
#     "table" : ["a piece of furniture", "list of facts & figures"]
# }

# print(word_meanings)

##you are given a list of subjects for students. assume one classroom is required for 1 subject.how many classrooms are needed by all students.
# subjects = {
#     "python", "java", "c++", "python", "javascript", "java",
#     "python", "java", "c++", "c"
# }
# print(len(subjects))

###wap to enter marks of 3 subjects from the user and store them in a dictonary.start with an empty dictionary & add one by one. use subjects name as key & marks as value.
# marks = {}

# x = int(input("enter phy : "))
# marks.update({"phy" : x})

# x = int(input("enter math : "))
# marks.update({"math" : x})

# x = int(input("enter chem : "))
# marks.update({"chem" : x})

# print(marks)

####figure out a way to store 9 & 9.0 as separate values in the set.
# values = {9, "9.25", 8, 8.0}
# print(values)

# values = {
#     ("float", 9.0),
#     ("int", 9)
# }
# print(values)