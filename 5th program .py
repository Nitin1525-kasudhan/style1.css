#LOOPS
#while True:
    #print("namste")

"""count = 1
while count<=5 :
    print("hello ")

    count = count+1
    print(count)"""

#  PRINT NUMBER FROM 1 TO 100 
"""i = 1 
while i <=1:
    print(i)

    i +=1"""

# PRINT NUMBER FROM 100 TO 1
"""i = 100 
while i <=1:
    print(i)

    i -=1"""
# multiplication of a number 
"""n = int(input("enter the number"))
i = 1
while i<=10:
    print(n*i)

    i+=1"""

#print the elements  of the following list using loops 
#[1,4,9,16,25,36,49,64,81,100]

"""nums = [1,4,9,16,25,36,49,64,81,100]

idx = 0 
while idx <len(nums):
    print(nums[idx])
    idx  +=1"""



# BREAK & CONTINUE

"""i = 0 
while i<=5:
    if(i == 3):
        i+=1
        continue
    print(i)
    i+=1 """


#for loop 
"""nums = [ 1,2,3,4,5]

for val in nums:
    print(val)"""

#range

"""seq = range(5)
for i in seq:
    print (i)"""



#start ,stop , step 
"""for i in range (2,10): #start ,stop 
    print (i)"""

#step
"""for i in range (2,20,2): #start ,stop,step 
    print (i)"""

#pass statement

for i in range(5):
    pass
print("some use full work")

# factorial of a number 
n = 5
fact = 1
i = 1
while i<=n:
    fact *=i
    i +=1

    print ("factorial= ",fact)