# Loops in python

# Loops are used to repeat the instruction

# We have 2 type of loops in python
# while Loop
# for loop


#Print the no 100 times forward and backward

# i = 1
# j=100
# while(i<=100):
#       print(i," ",j)
#       i=i+1
#       j=j-1

# multiplication of n no.

# i=1
# n = int(input("Enter the no. : "))
# print(n)
# print(type(n))
# while(i<=10):
#     print(n,"*",i,"=",i*n)
#     i*n
#     i=i+1 

# list itration

# i=0
# list1 = [21,3,4,56,12,5]

# while(i<=len(list1)-1):
#     print(list1[i])
#     i=i+1

# Search the no in list

n = int(input("enter the no : "))
i=0
k=0
list1 = [21,3,4,56,12,5]

while(i<=len(list1)-1):
    # print(list1[i])
    if(list1[i] == n):
        k=n
        break
        
    i=i+1

if(k==n):
    print("no is found")
else:
    print("no is not found")                



