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
def solution(s):
    frequency = {}
    for i in s:
        if i not in frequency:
            frequency[i] = 1
        else:
            frequency[i] +=1
    for i in range(len(s)):
        print("i",i)
        print("s[i]",s[i])
        if frequency[s[i]] == 1:
            return i
    return -1

# print(solution('alphabet'))
print(solution('barbados'))
# print(solution('crunchy'))