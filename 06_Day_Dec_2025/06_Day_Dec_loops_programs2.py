# Loops in Python
# Loops are used
# for sequential traversal. For traversing list, string, tuples etc

#-----------------
# for Loops
# list = [1, 2, 3]
# for el in list:
# for el in list:
# #some work
# print(el)
# for Loop with else
# for el in list:
# #some work
# for el in list:
# print(el)
# else:
# else:
# print("END")
#work when loop ends -----------

# list1 = [1,2,3,4,"hi","hello","monday","tuesday","wednesday",12.3,45.4]

# for x in list1:
#     print(x)

#-------Example of List---------

# fruits = ["Apple","Orange","Bannana"]
# for val in fruits:
#     print(val)

# #------Example of Touple-------

# tup = (1,2,3,4,"Hi","Hello")
# for val in tup:
#     print(val)   

# #------Exaple of String---------

# str = "Hello World"

# for val in str:
#     print(val)

#-----------wap to check the character in string----------
# ch = input('enter your character : ')
# str = input("Enter your string : ")
# print(str)
# for x in str:
#     if(x==ch):
#         print("found",x)
#         break
    
# else:
#     print("Not found")

#-----------------Search for a number x in this tuple using loop:
# num = int(input("Enter any no to search : "))
# tup = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)

# for i in tup:
#     if(i == num):
#         print("num is present" ,tup.index(i))
#         break
# else:
#     print("No is not available in touple")   

#----------Search for a number x in this list with index using loop----------    
# num = int(input("Enter any no to search : "))
# list = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

# for i in list:
#     if(i == num):
#         print("num is present" ,list[i])
#         break
# else:
#     print("No is not available in list") 

#----------------------------------------------------------------------
# range()
# Range functions returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
# range(start?, stop, step?)
# for el in range(5):
# print(el)
# for el in range(1, 5): print(el)
# for el in range(1, 5, 2): print(el)

# for x in range(5):  # default start with 0 (simple)
#     print(x)

# for x in range(2,5): #(start stop)
#     print(x)

# for x in range(2,20,2):
#     print(x)    

# Wap to find the even no between 5 to 10
start = 5
end = 10
count = 0

for x in range(start + 1, end, 2):
    print(x)
    count += 1

print("Count:", count)