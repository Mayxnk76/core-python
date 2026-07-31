# # Q1 print the even number between 1 to 100 using loop
#
# for i in range(2 , 101, 2):
#     print(i)
#
# # Q2 print the value is prime or not
#
# num = int(input("enter number: "))
#
# if num <= 1:
#     print("The number is not prime")
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             print("The number is not prime")
#             break
#     else:
#         print("The number is prime")
#
#
# """ Q3 Print the following pattern
#     1
#     1 2
#     1 2 3
#     1 2 3 4"""
#
# for i in range(1, 5):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()
#
# """ Q4 Print the following pattern
#    *
#   * *
#  * * *
# * * * *
# """
#
# for i in range(1, 5):
#     for j in range(5 - i):
#         print(" ", end="")
#     for k in range(i):
#         print("* ", end="")
#     print()
#
# # Q5 find the factorial of a number using loop
#
# f = int(input("enter a number: "))
#
# fact = 1
#
# for i in range(1, f + 1):
#     fact = fact * i
# print("factorial=",fact)
#
# # Q6 the number is even make table of it using loop
#
# num = int(input("enter number: "))
# if num % 2 == 0:
#    for i in range(1, 11):
#      print(num, "x", i, "=", num * i)
# else:
#     print("odd number")

