# illustratre arthimate operations (+,-,*,/)
# i1 = input("enter a 1 number")
# print(type(i1))
# i2  = input("enter 1 2 number")
# pls  = int(i1) + int(i2)
# minus  = int(i1) - int(i2)
# mu = int(i1) * int(i2)
# div  = int(i1) / int(i2)
# print(pls)
# print(minus)
# print(mu)
# print(div)


# find prime number or not

# def is_prime(number):
#     if number > 0:
#         for num in range(2,number):
#             if number%2 == 0:
#                 return ("not prime number")
#         return ("prime number")   
#     return ("not prime number")        

# print(is_prime(10))     

#PALINDROME NUMBER PROGRAM IN PYTHON 
# a = '151'
# b = a[::-1]
# if a ==b:
#     print("pandl")
# print('not pandl')

# swap two numbers
# i1 = input("enter a 1 number")
# i2 = input("enter a 2 number")
# temp = 0
# temp = i1
# i1 = i2
# i2 = temp
# print(i1,i2)

# find max number without inbuily fun
# a =  10
# b = 20
# print(max(a, b))
# if a > b:
#     print(f'{a} is greater than {b}')
# else:
#     print(f'{a} is less than {b}')    


#Given an array nums, write a function to move all zeroes to the end of it while maintaining the relative order of 
#the non-zero elements.

# array1 = [0,1,0,3,12]
# array2 = [1,7,0,0,8,0,10,12,0,4]

# def solution(nums):
#     for i in nums:
#         if 0 in nums:
#             print("checking o is their in last or not",i)
#             print("nums",nums)
#             nums.remove(0)
#             print("nums",nums)
#             nums.append(0)
#             print("nums",nums)
#     return nums

# solution(array1)
# solution(array2)    


# Given a string, find the first non-repeating character in it and return its index. 
# If it doesn't exist, return -1. # Note: all the input strings are already lowercase.

#Approach 1
# def solution(s):
#     frequency = {}
#     for i in s:
#         if i not in frequency:
#             frequency[i] = 1
#         else:
#             frequency[i] +=1
#     for i in range(len(s)):
#         print("i",i)
#         print("s[i]",s[i])
#         if frequency[s[i]] == 1:
#             return i
#     return -1

# # print(solution('alphabet'))
# print(solution('barbados'))
# print(solution('crunchy'))

# problems

########### reverse a interger 


# n = int(input("please give a number : "))
# print("before reverse your numeber is : %d" %n)
# reverse = 0
# while n!=0:
#     print("n",n)
#     print("reverse",reverse)
#     reverse = reverse*10 + n%10  
#     print("revers4e",reverse)     
#     n = (n//10)
#     print("n1",n)
# print("After reverse : %d" %reverse) 

########## check given number is amstrong number or not
# n = int(input('pls enter a number'))
# b = len(str(n))
# s  = n
# sum1 =0
# while n!=0:
#     r = n%10
#     sum1 = sum1 + (r**b)
#     n = n//10
# print("sum1",sum1)
# if s == sum1:
#     print("given number is a armstorn number")
# else:
#     print("given number is not a armstrong number")        
    

######## Check givrn number is a prime or not
    
# number = int(input('pls enter a number to find prime number'))
# if number>1:
#     print("entering")
#     for num in range(2,number): # if stop is less than start in range it doesnt do loop it goes to else
#         print("checking",num,number)
#         if number%num == 0:
#             print("number is not a prime number")                                                                             
#     else: # this is very important 
#         print("number is a prime number")
            
    

############ fibanic series with recursion method

# recursion is calling its function inside the function

# n  = int(input("pls enter a number for to test fibannic series"))
# def fib(i):
#     if i == 0:
#         return 0
#     if (i == 1 or i == 2):
#         return 1
#     else:
#         fibanic_number  = fib(i-1) + fib(i-2)
#         if i == 3:
#             print("checking",i,fib(i-1), fib(i-2))
#         # print("fibanic seres",fibanic_number)
#         return fibanic_number

# for i in range(0,n):
#     print(fib(i))        
        

######### fibannic series by using iterative method
# n  = int(input("pls enter a number for to test fibannic series"))
# a,b =0,1
# for i in range(0,n):
#     if i<=1:
#         print(i)
#     else:
#         res = a+b
#         a =b
#         b = res
#         print("tres",res)    

############# check a number is palindrome by using itrative method
# n  = int(input("pls enter a number for to test palindrome series")) 
# rev = 0
# temp = n
# while temp!=0:
#     rev = rev*10 + temp%10
#     temp = temp//10
# print("outpu",rev,"n",n)      
# if rev == n:
#     print("palindrone number")
# else:
#     print("not palindroine")    

########## find a number is binary or not
# n = int(input("pls enter a number to find it is binary ot not"))
# while n!=0:
#     j = n%10
#     if j!=0 and j!=1:
#         print("not binary")
#         break
#     n = n//10
#     print("n",n)
#     if n== 0:
#         print("binary number")

######### swap a integer by third varible
# a = 10
# b = 20
# temp = 0

# temp  = a
# a  =b
# b = temp
# print("a,b",a, b)


############ write a nunber find the sum of digits of number by using recursion
# n = int(input("pls enter a numbers to find factor of number"))

# for i in range(1,n+1):
#     if n%i == 0:
#         flag = 0
#         for j in range(2,i):
#             if i%j == 0:
#                 flag = 1
#                 break
#         if flag == 0:
#             print("prime number ",i) 

############ adding two integers without using arthmatic operatrs

# def add(x,y):
#     while(y!=0):
#         carry = x & y 
#         print("carry",carry) 
#         x  = x^y
#         print("x",x)
#         y = carry << 1
#         print("y",y)
#     return x
# print("add",add(52,13))    


############ find given number is perfect or not

# n = int(input("pls enter a number "))
# sum1  = 0
# for i in range(1,n):
#     if n%i ==0 :
#         sum1 = sum1 + i
# print("sum1",sum1)
# if sum1 == n :
#     print("given number is a perfect number")

######## Python Program to find the Average of numbers with explanations.
# from statistics import mean
# a = [1,2,3,4,5,9,109]
# avg = mean(a)
# # avg = sum(a)/len(a)
# print("avg",round(avg,1))    
            
######## Python Program to calculate factorial using iterative method.
# n =int(input("pls enter a number"))
# factorial  =1
# for i in range(1, n+1):
#     # print("checking",i)
#     factorial = factorial * i
#     print("fac",factorial)    
    


########### check given number is even or odd

# n =int(input("pls enter a number"))
# if n%2 == 0:
#     print("given number is even ")
# else:
#     print("given number is odd")  
       

######### Python program to print first n Prime Number with explanation.      

# n =int(input("pls enter a number for first n prime number "))  
# first_prime_number = 1
# if n>1:
#     for i in range(2,n):
#         if n%i == 0:
#             print("i",i)
#             first_prime_number = i
#             break
#     else:
#         print("entering")
#         first_prime_number = n
# print("first n number",first_prime_number)        
 
 
########### find the power by using pow methods
# base = int(input("take base number"))
# exponent = int(input("take exponent numnber"))

# power = pow(base,exponent)   

# print("power number", power)        


########### find the power by using for loop
# base = int(input("take base number"))
# exponent = int(input("take exponent numnber"))
# power = 1
# for i in range(0,exponent):
#     power = power * base
# print("power",power)    
           
########### find the power by using while loop
# base = int(input("take base number"))
# exponent = int(input("take exponent numnber"))     

# power  =1
# while (exponent!=0):
#         power = power * base
#         exponent -=1
# print("power",power)        


###########3 find smallest number among three
# a = 10
# b =20
# c= 15
# if a <=b and  a <=c:
#     print("a",a)   
# if b <=c and  b <=a:
#     print("b",b)   
# if c <=a and  c <=b:
#     print("c",c)                  
           
#########Python Program to calculate the square of a given number. 
# n = int(input("take number to find square"))   
# square = n*n
# print("square",square)    


# a  = [1,3,4,4,5]
# for i in range(len(a)):
#     print("i",i)    

# a  = 10
# b = "1" * a
# print("b",b,type(b))


############## generators
# def top_ten_squares(n):
#     print("satreting")
#     while n!=0:
#         s  = n*n
#         n -=1
#         yield s

# s = top_ten_squares(10) 
# print("caliing")
# print("iteraytor location",id(s))
# for i in s:
#     print("i",i)       


######### find given number is sum of two number in list is equal or not

# n = 9
# l = [1,4,7,5,7,1,2]    
# flag = 0
# for i in range(len(l)):
#     print("checking1.py")
#     if flag == 0:
#         for j in range(i+1,len(l)):
#             print("i",l[i])
#             print("j",l[j])
#             if l[i] + l[j] == n:
#                 print(True)
#                 flag = 1
#                 break
#     else:
#         break        

########### interchange first and last elements in the list
# l = [1,2,3,4,10]     
# temp = l[0]
# l[0] = l[-1]
# l[-1] = temp
# print("l",l,len(l))

########## finding the length of list in different ways
# l = [1,2,3,4,10] 
# counter = 0
# for i in range(len(l)):
#     counter = counter + 1

# print("counter",counter)   

######### find smallest number in the list
# l = [11,2,3,4,10]
# smallest = l[0]
# for i in l:
#     if i < smallest:
#         smallest = i
# print("smallest number",smallest)           

######### find largest number in the list
# l = [11,2,3,4,110]
# largest = l[0]
# for i in l:
#     if i > largest:
#         largest = i
# print("largest number",largest)       

############ slicing operations
# a = [12,3,4,5,11,6,7,21,8,19,20]
# #1
# print(a[0])
# # 2
# print(a[-1])
# # 3
# print(a[:])
# # 4
# print(a[2:])
# # 5
# print(a[:2])
# # 6
# print(a[3:6])
# #7 intervals
# print(a[2:9:3])
# #8 intervals
# print(a[-2:-9:-3])


########## seperate only duplicates in the list
# l = [1,2,3,4,5,6,7,8,6,2]
# new_list = []
# dupl_list = []
# for i in l:
#     print("i",i)
#     if i in new_list:
#         dupl_list.append(i)
#     else:
#         new_list.append(i)    
# print("duplist",dupl_list)    

# dup = list({x for x in l if l.count(x)>1})
# print("dup",dup)

########### find n largest numbers in a list

# def findnlargest_numbers(lst, n):
#     final_lst = []
#     for i in range(0,n):
#         max1 = 0
#         for j in range(len(lst)):
#             if lst[j] > max1:
#                 max1 = lst[j]
#         lst.remove(max1)
#         final_lst.append(max1)
#     print(final_lst)    
        

# n =2 
# lst = [1,32,4,4,56,56,7]               
# print(findnlargest_numbers(lst,2)) 
    

##########Python program to print all even numbers in a range
# for i in range(1,101):
#     if i%2 ==0:
#         print("odd number in ranme",i)

######## print postive numbers in a range
# start = -4
# end  =10
# for i in range(start,end+1):
#     if i>=0:
#         print("i",i)
        
######## print negative numbers in a range
# start = -4
# end  =10
# for i in range(start,end+1):
#     if i<0:
#         print("i",i)

########### remove multiple items in a list
# lst = [1,2,3,4,5]
# remo  = [1,2]
# for i in remo:
#     lst.remove(i)
# print("new itesm",lst)    

######## divide list into given number chunk

# def divide_chunk_lst(lst,n):
#     for i in range(0,len(l),n):
#         print("i",i)
#         yield l[i:i+n]
# l = ['a','b','c','d','e','f','g','h','i','j']
# n = 3 
# x  = list(divide_chunk_lst(l,n))
# print("x",x)


############ Reverse words in a given String in Python
# s = "hellpo how are you"
# sp = s.split()[::-1]
# new_s= " ".join(sp)
# print("new_s",new_s)

###### Ways to remove i’th character from string in Python
# s = "helloamshaikhafeez"
# n =3
# item  = s[n] 
# new_s = s.replace(item, '')
# print("new_s",new_s)

######## Python program to print even length words in a string
s = "hellpo how are you"
l = s.split(" ")
print("l",l)
for i in l:
    if len(i)%2 == 0:
        print("even words",i)