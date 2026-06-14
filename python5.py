##loops in python
#while loop
# while True :
#     print("hello")

# count = 1
# while count <= 5 :
#     print("hello")
#     count += 1

# i = 1
# while i <= 5:
#     print("Naveen")
#     i+=1

#print numbers from 1 to 5   
# i = 1
# while i <=5:
#     print(i)
#     i += 1
# print("loop ended")

# i = 5
# while i >= 1:
#     print(i)
#     i -= 1
# print("loop ended")

##########
##print numbers from 1 to 100.
# i = 1
# while i <= 100:
#     print(i)
#     i += 1

##print numbers from 100 to 1.
# i = 100
# while i >= 1:
#     print(i)
#     i -= 1

##print the muliplication table of a number n.
# i = 1
# while i <= 10:
#     print(3*i)
#     i += 1

# n = int(input("enter number : "))
# i = 1
# while i <= 10:
#     print(n*i)
#     i += 1

##print the elements of the following list using a loop.
# nums = [1,4,9,16,25,36,49,64,81,100]

#  idx = 0
#  while idx < len(nums):
#      print(idx)
#      idx += 1

# i = 0
# while i < len(nums):
#     print(nums[i])
#     i += 1

# heros = ["allu arjun","prabhas","mahesh babu","ram charan"]
# i = 0
# while i < len(heros):
#     print(heros[i])
#     i += 1

##search for a number x in this tuple using loop.
# nums = (1,4,16,25,36,49,64,81,100)

# i = 0
# while i < len(nums):
#     print(nums[i])
#     i += 1


##break and continue
#break 
# i = 1 
# while i <= 5:
#     print(i)
#     if(i == 3):
#         break
#     i += 1

# print("end of loop")

#continue 

# i = 0
# while i <= 5:
#     if(i == 3):
#         i += 1
#         continue
#     print(i)
#     i += 1

#odd 
# i = 1
# while i <= 10:
#     if(i%2 == 0):
#         i += 1
#         continue
#     print(i)
#     i += 1

#even
# i  = 0
# while i <= 10:
#     if(i%2 != 0):
#         i += 1
#         continue
#     print(i)
#     i += 1 

#Loops in python.

# tuo = (1, 9, 2, 8, 3, 7, 4, 6, 5)

# for num in tuo:
#     print(num)

# str = "Naveen"
# for char in str:
#     print(char)

######
#print the elenents of the following list using a loop.
# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for el in nums:
#     print(el)

##search for a number x in this tuple using loop:
# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)
# x = 49

# idx = 0
# for el in nums:
#     if(el == x):
#         print("number found at idx", idx)
#     idx += 1

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49]
# x = 49

# idx = 0
# for el in nums:
#     if(el == x):
#         print("number found at idx", idx)
#         break
#     idx += 1

##Range()
# seq = range(10)
# for i in seq:
#     print(i)

# for i in range(10):
#     print(i)

# for i in range(2, 10): 
#     print(i)

# for i in range (2, 10, 2):
#     print(i)

# for i in range(1,100, 2):
#     print(i)

################
#print numbers from 1 to 100.
# for i in range(1, 101):
#     print(i)

##print numbers from 100 to 1.
# for i in range(100, 0, -1):
#     print(i)

###print the multiplication table of a number n.
# n = int(input("enter number : "))
# for i in range(1, 11):
#  print(n * i)

#Pass statement.
# for i in range(5):
#  pass
# print("some useful work")

################
#Wap to find the sum of first n numbers.(using while).
# n = 9
# sum = 0
# for i in range(1, n+1):
#   sum += i
# print("total sum =", sum)

#Wap to find the factorial of first n numbers.(using for).
# n = 7
# sum = 0
# i = 1
# while i <= n:
#   sum += i
#   i += 1 n    
# print("total sum =", sum)

##Wap to find the factorial of first n numbers.(using for).
# n = 7
# fact = 1
# i = 1
# while i <= n:
#   fact *= i
#   i += 1     
# print("factorial =", fact) 

##for while
# n = 5
# fact = 1

# for i in range(1, n+1):
#   fact *= i   
# print("factorial =", fact) 


