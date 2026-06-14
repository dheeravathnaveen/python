#lists in python

# marks = [94.5, 87.6, 95.3, 66.3, 45.2]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(len(marks))

# student = ["Naveen",94.5,18,"Hyd"]
# print(student)
# student[0] = "Anand"

#list slicing
# marks = [85,94,76,63]
# print(marks[1:3])

#list methods
# list = [2,1,3]
# list.append(4)
# print(list)

# list = [2,1,3]
# print(list.append(4))
# print(list.sort())
# print(list)

#list = [2,1,3]
# print(list.append(4))
# print(list.sort(reverse=True))
# print(list)

# list = ["Naveen","hari","anand"]
# print(list.sort(reverse=True))
# print(list)

# list =['a','d','e','f','c']
# print(list.sort())
# print(list)

# list =['a','d','e','f','c']
# list.reverse()
# print(list)

# list = [2,1,3]
# list.insert(1,5)
# print(list)

# list = [2,1,3,6,9]
# list.pop(2)
# print(list)

#tuples in python
# tup =()
# tup =(1)
# tup =(1.0)
# tup =(1,)
# tup =("hello")
# tup =("hello",)
# tup = (1,2,3,4,)
# print(tup)
# print(type(tup))
# tup =(1,2,3,4,5)
# print(tup[1:3])

# tup = (1,2,3,4,2,2,2,1)
# print(tup.count(2))

#############
#wap to ask the user to enter names of their 3 fav movies and store them in a list.

# movies = []
# mov1 = input("enter 1st movie: ")
# mov2 = input("enter 2nd movie: ")
# mov3 = input("enter 3rd movie: ")

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)

# print(movies)

#wap to check if list contains a palindrome of elements.

# list1 = [1, 2, 1]
# list1 = [1, 2, 3]

# copy_list1 = list1.copy()
# copy_list1.reverse()

# if copy_list1 == list1:
#     print("palindrome")
# else:
#     print("NOT PALINDROME")

# list1 = ["m", "a", "a", "m", "p"]

# copy_list1 = list1.copy()
# copy_list1.reverse()

# if(copy_list1 == list1):
#     print("palindrome")
# else:
#     print("NOT PALINDROME") 

#wap to count the number of students with the "A" grade in the following tuple.

# grade = ["C", "D", "A", "A", "B", "B", "A"]
# grade.sort()
# print(grade)