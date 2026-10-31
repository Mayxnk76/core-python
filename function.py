## 1)Take user input and create a menu driven program to perform mathematical 
## operations like addition, subtraction, multiplication, division, integer 
## division, power. Return values from the functions
# def addition(a,b):
#     return a + b
# def subtraction(a,b):
#     return a - b
# def multiplication(a, b):
#     return a * b
# def divition (a, b):
#     return a / b
# def int_div(a, b):
#     return a // b
# def power(a, b):
#     return a ** b

# a = float(input("enter first number:"))
# b = float(input("enter second number:"))

# print("\n---- Calculator Menu ----")
# print("1. Addition")
# print("2. Subtraction")
# print("3. Multiplication")
# print("4. Division")
# print("5. Intteger Division")
# print("6. Power")

# choice = int(input("enter your choice:"))

# if choice == 1:
#     result = addition(a,b)
# elif choice == 2:
#     result = subtraction(a,b)
# elif choice == 3:
#     result = multiplication(a, b)
# elif choice == 4:
#     if b != 0:
#         result = divition(a, b)
#     else:
#         result = "Cannot divide by zero"
# elif choice == 5:
#     if b != 0:
#         result = int_div(a, b)
#     else:
#         result = "Cannot divide by zero"
# elif choice == 6:
#     result = power(a, b)
# else:
#     result = "Invalid choice"
    
# print("Result:",result)

# #2)Create functions to calculate 																																																
# #Area of a rectangle = width * length
# #Area of a triangle = ½ * Height * Base
# #Area of a circle = pi*r*r

# import math

# def rectangle(width,length):
#     return width * length

# def triangle(height,base):
#     return 0.5 * height * base 

# def circle(r):
#     return math.pi*r*r

# width = float(input("Enter rectangle width:"))
# length = float(input("Enter triangle base:"))

# height = float(input("Enter triangle height:"))
# base = float(input("Enter triangle base:"))
# r = float(input("Enter circle redius:"))

# print("Area of Reactangle:",rectangle(width, length))
# print("Area of Triangle:",triangle(height, base))
# print("Area of Circle:",circle(r))

# # 3)Create functions to convert decimal numbers to binary, octal and 
# # hexadecimal numbers. Always return values from the functions

# def binary(n):
#     return bin(n)
# def octal(n):
#     return oct(n)
# def hexadecimal(n):
#     return hex(n)

# num = int(input("Enter a decimal number:"))

# print("Binary:",binary(num))
# print("Octal:",octal(num))
# print("Hexadecimal:",hexadecimal(num))

# # 4)Write a udf to find the length of the given 
# # string without using the len function.

# def string_length(s):
#     count = 0
#     for ch in s:
#         count += 1
#     return count

# s = input("Enter a String:")
# print("Length:",string_length(s))

# # 5)Write a UDF to reverse a given number.
# def reverse_number(n):
#     rev = 0
#     while n > 0:
#         digit = n % 10
#         rev = rev * 10 + digit
#         n = n // 10
#     return rev
# n = int(input("Enter a number:"))
# print("Reverse:",reverse_number(n))

# # 6)Write an UDF to return a list having only 
# # unique values by removing duplicate values 
# # from the provided input list.

# def unique_list(lst):
#     unique = []
#     for i in lst:
#         if i not in unique:
#             unique.append(i)
#     return unique
# lst = [1,2,3,4,5,6,7,8,3,3,5,5]
# print("Unique List:",unique_list(lst))

# # 7)Write a Python function to multiply all the numbers in a list.

# def multy_list(lst):
#     result = 1
#     for i in lst:
#         result = result * i
#     return result
# lst = [2,3,4,5]
# print("Multiplication:",multy_list(lst))

# # 8)Write a UDF to check the inputted number is between specified range or not.
# def check_range(num,start,end):
#     if start <= num <= end:
#         return True
#     else:
#         return False

# num = int(input("enter a number:"))
# start = int(input("enter starting range:"))
# end = int(input("enter ending range:"))

# if check_range(num, start, end):
#     print("Number is within range")
# else:
#     print("Number is not within range")

# # 9)Write a function to calculate total number 
# # of Uppercase and lowercase characters in the string.

# def count_case(s):
#     upper = 0
#     lower = 0
    
#     for ch in s:
#         if ch.isupper():
#             upper += 1
#         elif ch.islower():
#             lower += 1
            
#     return upper,lower

# s = input("Enter a string:")
# u,l = count_case(s)

# print("Uppercase:",u)
# print("Lowercase:",l)


# # 10)Write an UDF to check if the user given number is a prime number or not.
# # Using lambda
# def prime(n):
#     if n <= 1:
#         return False
#     for i in range(2,n):
#         if n % i == 0:
#             return False
#     return True
# n = int(input("enter a number:"))
# if prime(n):
#     print("Prime Number")
# else:
#     print("Not a Prime Number")
# # 1)Create a lambda function that will return maximum of two numbers
# maximum = lambda a,b:a if a > b else b

# a = int(input("enter first number:"))
# b = int(input("enter second number:"))

# print("Maximum:",maximum(a,b))
# # 2)Create a lambda function that will return maximum of three numbers
# maximum = lambda a,b,c:a if a > b and a > c else(b if b > c else c)

# a = int(input("Enter first number:"))
# b = int(input("Enter second number:"))
# c = int(input("Enter third number:"))

# print("Maximum:",maximum(a,b,c))

# # 3)Write a lambda function that takes one number and if the number is even, returns that number multiplied by 5 else if the number is odd, returns that number multiplied by 10
# result = lambda n:n * 5 if n % 2 == 0 else n * 10

# n = int(input("enter a number:"))
# print("Result:",result(n))

# # 4)Create a calculator using lambda functions

# add = lambda a,b: a + b
# sub = lambda a,b: a - b
# mul = lambda a,b: a * b
# div = lambda a,b: a / b
# mod = lambda a,b: a % b
# power = lambda a,b: a ** b

# a = float(input("Enter first number:"))
# b = float(input("enter second number:"))

# print("1. Addition")
# print("2. Subtraction")
# print("3. Multiplication")
# print("4. Division")
# print("5. Modulus")
# print("6. Power")

# ch = int(input("Enter your choice:"))

# if ch == 1:
#     print("Result:",add(a,b))
# elif ch == 2:
#     print("Result:",sub(a,b))
# elif ch == 3:
#     print("Result:",mul(a,b))
# elif ch == 4:
#     if b != 0:
#         print("Result:", div(a, b))
#     else:
#         print("Cannot divide by zero")
# elif ch == 5:
#     if b != 0:
#         print("Result:", mod(a, b))
#     else:
#         print("Cannot divide by zero")
# elif ch == 6:
#     print("Result:",)
# else:
#     print("Invalid Choice")