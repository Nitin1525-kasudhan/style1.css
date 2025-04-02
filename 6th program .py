# function and recursion

#function definition
"""def sum (a,b):#parameters
    s = a+b
    return s 
print(sum(2,5))"""#arguments


#many time use the same cade 
"""def calc_sum (a,b): 
    sum = a+b
    print(sum)
    return sum


calc_sum(16,28)#function call



calc_sum(43,23;)"""

#same line with space
#print("nitin",end=" ")
#print("kasaudhan")

#WAP to print the length of a list.(list in parameter)
"""cities =("delhi","gorgaon","gorakhur")
heroes = ("thor","ironman")

def print_len(list):
    print(len(list))


print_len(cities)
print_len(heroes)"""


#WAF to print the element of a list in a single line .(list in the parameters)
"""cities =("delhi","gorgaon","gorakhur")
heroes = ("thor","ironman")

def print_len(list):
    for item in list:
        print(item,end=" ")

print_len(heroes)"""

#factorial of a number 
"""def cal_fact(n):
    fact = 1
    for i in range (1,n+1):
        fact*=i
        print(fact)

cal_fact(5)""""""

# RECUSION 
"""def show (n):
    if (n == -100):# base case 
        return
    print(n)
    show(n-1) 
show (0) """

# factorial of a number by using recursion 

"""def fact(n):
    if (n == 1 or n == 0):
        return 1 
    return fact(n-1)*n"""

print(fact(1))

#WAP a recersive function to calculate the sum of frist n naturl number 
"""def calc_sum(n):
    if (n ==0 ):
        return 0
    return calc_sum(n-1)+n

    
"""sum = calc_sum(50)
print(sum )"""
