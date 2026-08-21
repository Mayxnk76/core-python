# UNIT 1
# Basic Programming

# Q1 Write a python program to print "Hello World"

print("Hello World")

# Q2 Write a python program to get user input using input( ) function

name = input("enter your name:")
print(name)

# Q3 WAP to take only numerical input.

num = int(input("enter number :"))
print(num)

# Q4 Convert the number to floating point number.

num = 45
print(float(num))

# Q5 WAP to Add, Subtract, Multiply and Divide 2 numbers.

num1 = int(input("enter 1st number:"))
num2 = int(input("enter 2nd number:"))

print("The addition is :", num1 + num2)

# Q6 Print the quotient and remainder separately for division operation.

num1 = int(input("enter 1st number:"))
num2 = int(input("enter 2nd number:"))

quotient = num1 / num2
remainder = num1 % num2

print("the quotient is :",quotient)
print("the remainder is :",remainder)

# Q7 Write a program to find meter to kilometer.

num = int(input("enter meter value:"))
print("meter into KM : ",num/1000,"Km.")

# Q8 Write a program to find area of a rectangle.

l = eval(input("Enter value of L:"))
b = eval(input("Enter value of B: "))

area = l * b

print("The Area of Rectangle is :",area)

# Q9 Write a program to find volume of cube.

l = eval(input("Enter value of L:"))
b = eval(input("Enter value of B:"))
h = eval(input("enter value of H:"))

cube = l*b*h

print("The Area of Cube is :",cube)

# Q10 write a program to find area of triangle.

l = eval(input("Enter value of L:"))
b = eval(input("Enter value of B:"))

triangle = (l*b)/2

print("The area of triangle is :",triangle)

# Q11 WAP to convert the given temperature from Fahrenheit to Celsius

f = eval(input("enter the value of fahrenheit:"))

c = (f - 32)/1.8

print("the calsius is :",round(c,2),"c")

#Q12 WAP to convert temperature from Celsius to Fahrenheit where temperature
# in Celsius is entered by user.

c = eval(input("eneter value of celsius :"))

f = c*(9/5)+32

print("the Fahrenheit is : ",f)

# Q14 Take a number as user input and convert it into Binary, Octal and
# Hexadecimal numbers

num = eval(input("enter the number in decimal :"))

print("the binary number is :",bin(num))
print("the octal number is :",oct(num))
print("the hexadecimal number is :",hex(num))

# Q14 Take binary, octal and hexadecimal numbers as an input
# and convert them to Decimal number

binary = input("enter BInary number :")
octal = input("enter octal number :")
hexa = input("enter hexadecimal number :")

print("the binary number to decimal is :",int(binary, 2)) # use 2 for binary number
print("the octal number to decimal is :",int(octal, 8)) # use 8 for octal number
print("the hexadecimal to decimal number is :",int(hexa, 16)) # use 16 for hexa decimal value

# Q15 Take 3 different inputs from user and display their data type.

num1 = int(input("enter 1st number :"))
num2 = float(input("enter 2nd number :"))
num3 = input("enter your name :")

print("the data type of 1st number is :",type(num1))
print("the data type of 2nd number is :",type(num2))
print("the data type of 3rd number is :",type(num3))

# Q16 Perform binary "AND" and "OR" operation for given 2 integer numbers from user input(for python)

num1 = int(input("enter 1st number: "))
num2 = int(input("enter 2nd number: "))

print("Binary AND :",num1 & num2)
print("Binary OR :",num1 | num2)

# Q17Write a program to calculate area of circle. (pi*r*r)

r = int(input("eneter value of R :"))
pi = 3.14

print("the area of circle is :", pi*r*r)

# Q18 Write a program in C to calculate simple interest

p = int(input("enter value of P ="))
r = int(input("enter value of R ="))
n = int(input("enter value of N ="))

si = (p*r*n)/100

print("the simple intrest is :",si)

# Q19 Without applying condition statement display output as “true” if a number is
# an even number and “false” if the number is an odd number

num = int(input("enter a number:"))
print(str(num % 2 == 0))

# Q20 Write a program to swap two numbers using a third variable and also
# without using the third variable.

a = int(input("enter first number:"))
b = int(input("enter second number:"))
# using 3rd variable
c = a
a = b
b = c
print("after swap:",a,b)
#without using third variable
a,b = b,a

print("after swap:", a,b)

# Q21 Write a program to display the operations of bitwise AND and bitwise OR
# on two numbers entered by the user

num1 = int(input("enter 1st number: "))
num2 = int(input("enter 2nd number: "))

print("Binary AND :",num1 & num2)
print("Binary OR :",num1 | num2)

# Q 22

x = 100
y = 200

print(x and y)
print(x or y)


