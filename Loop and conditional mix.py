# # 1) Write a program to check whether the given number is Armstrong or not?
#
# num = int(input("enter nuber to check armstrong number :"))
#
# original = num
# digits = len(str(num))
# sum = 0
#
# while num > 0:
#     digit = num % 10
#     sum = sum + digit ** digits
#     num = num // 10
#
# if sum == original:
#     print("the number is armstrong number:",original)
# else:
#     print("the number is not armstrong number:", original)
# from operator import truediv
# from string import digits
# from sys import flags

# # Q2 Write a program to enter two numbers and print all the Armstrong numbers between
# # those two numbers
#
# start = int(input("enter 1st number :"))
# stop = int(input("enter 2nd number :"))
#
# for num in range(start, stop + 1):
#     original = num
#     digits = len(str(num))
#     sum = 0
#
#     while num > 0:
#         digit = num % 10
#         sum = sum + digit ** digits
#         num = num // 10
#
#     if sum == original:
#         print(sum)

# # Q3) Write a program to find the factorial of the given number
#
# num = int(input("enter number to finde a factorial :"))
#
# fact = 1
#
# for i in range(1, num + 1):
#     fact = fact * i
#
# print("the factorial of",num,"is :", fact)

# # Q4 Write a program to print the factorial of all the given numbers between the two given
# # numbers
#
# num = int(input("enter 1st number :"))
# num1 = int(input("enter last number :"))
#
# for i in range(num + 1, num1):
#     fact = 1
#
#     for j in range(1, i + 1):
#         fact = fact * j
#
#     print(i ,"=",fact)

# #Q5) Write a program to check whether the given number is prime or not
#
# num = int(input("enter a number to check prime or not :"))
#
# if num <= 1:
#     print("the number is not prime")
# else:
#     flag = True
#
#     for i in range(2, num + 1 ):
#         if num % 2 == 0 :
#             flag = False
#             break
#
#     if flag == True:
#         print("the number is prime ")
#     else:
#         print("the number is not prime")

# Q6Write a program to print all the prime numbers between 1 and 100.

for num in range(2, 101):
    flag = True

    for i in range(2, num):
        if num % i == 0:
            flag = False
            break
    if flag == True:
        print(num)

# # 7) Write a program to print the following pattern
# # 1
# # 2 1
# # 1 2 1
# # 2 1 2 1
# # 1 2 1 2 1
# for i in range(1, 6):
#     for j in range(i):
#         if((i - j)% 2 == 0):
#             print(2,end=" ")
#         else:
#             print(1,end=" ")
#     print()
# #  second trick for do this pattern:
# x = 1
# for i in range(1, 6):
#     for j in range(i):
#         print(x,end=" ")
#
#         if x == 1:
#             x = 2
#         else:
#             x = 1
#     print()