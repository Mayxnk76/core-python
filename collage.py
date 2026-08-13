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

# Q10 rite a program to find area of triangle.

l = eval(input("Enter value of L:"))
b = eval(input("Enter value of B:"))

triangle = (l*b)/2

print("The area of triangle is :",triangle)



