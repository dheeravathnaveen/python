#strings

# str1 = "apna"
# len1 = len(str1)
# print(len1)

# str2 = "college"
# len2 = len(str2)
# print(len2)

# final_str = str1 +" "+ str2
# print(final_str)
# print(len(final_str))

#indexing
# str = "python"
# ch = str[3]
# print(ch)

#slicing
# str = "python programming"
# print(str[3:5])
# print(str[:6])
# print(str[7:]) 

##str.endswith("er.")
# str = "welcome to python programming"
# print(str.endswith("ing"))

##str.capitalize()
# str = "welcome to python programming"
# print(str.capitalize())
# print(str)  

##str.replace(old, new)
# str = "welcome to python programming"
# print(str.replace("o", "a"))
# print(str.replace("python", "java"))

##str.find(word)
# str = "welcome to python programming"
# # print(str.find("m"))
# print(str.find("python"))

##str.count("am")
# str = "welcome to python programming"
# print(str.count("o"))

#############
##wap to input user's name and print its length
# print(len(input("Enter your name :")))

##wap to find the occurrence of "s" in the string.
# str = "hi, $iam the $ symbol $99.99"
# print(str.count("$"))

#conditonal statements
# age = 20

# if(age >= 18):
# if(True):
#    print("can vote")
#    print("can drive")     

# lights = "green"

# if(lights == "red"):
#     print("stop")
# elif(lights == "green"):
#     print("go")
# elif(lights == "yellow"):
#     print("wait")

# print("end of code")    

# num = 10
# if(num > 2):
#     print("num is greater than 2")
# if(num > 5):
#     print("num is greater than 5")
# elif(num > 8):
#     print("num is greater than 8")

#conditional statements

# marks = int(input("Enter the marks of the student ->"))
# if(marks >= 90):
#     Grade = "A"
# elif(marks >= 80 and marks < 90):
#     Grade = "B"
# elif(marks >= 70 and marks < 80):
#     Grade = "C"
# else:
#     Grade = "D"

# print("grade of the student ->", Grade)

#nesting

# age = 22

# if(age >= 18):
#     if(age >= 30):
#         print("cannot drive ")
#     else:   
#         print("can drive")
# else:
#     print("cannot drive")




###########
#wap to check if a number entered by the user is odd or even.
# num = int(input("Enter a number :"))
 
# if num % 2 == 0:
#      print("Even")
# else:
#      print("Odd")

#wap to find the grestest of 4 numbers entered by the user

# a = int(input("Enter first number :"))
# b = int(input("Enter second number :"))
# c = int(input("Enter third number :"))  
# d = int(input("Enter fourth number :"))
# if (a >= b and a >= c):
#     print("first number is largest ", a)
# elif (b >= c):
#     print("second number is largest ", b)
# elif (c >= a and c >= d):
#     print("third number is largest ", c) 
# else:
#     print("fourth number is largest ", d)
    
#wap to check if a number is multiple of 7 or not.

# x = int(input("Enter a number :"))

# if(x % 7 == 0):
#     print("Multiple of 7")
# else:
#     print("Not a multiple of 7")