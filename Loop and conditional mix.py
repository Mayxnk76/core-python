# 1) Write a program to check whether the given number is Armstrong or not?

num = int(input("enter nuber to check armstrong number :"))

original = num

# Count the number of digits
# Example: 153 has 3 digits
digits = len(str(num))
sum = 0
# Extract each digit one by one
while num > 0:
    # Get the last digit of the number
    # Example: 153 % 10 = 3
    digit = num % 10
    # Add the digit raised to the power of number of digits
    # Example: 3³, 5³, 1³
    sum = sum + digit ** digits
     # Remove the last digit
    # Example: 153 // 10 = 15
    num = num // 10

if sum == original:
    print("the number is armstrong number:",original)
else:
    print("the number is not armstrong number:", original)

# Q2 Write a program to enter two numbers and print all the Armstrong numbers between
# those two numbers

start = int(input("enter 1st number :"))
stop = int(input("enter 2nd number :"))

# Check every number from start to stop
for num in range(start, stop + 1):
     # Store the original number because num will change in while loop
    original = num
    # Count the number of digits
    # Example: 153 has 3 digits
    digits = len(str(num))
    # Variable to store the sum of powered digits
    sum = 0

    # Extract each digit one by one
    while num > 0:
        # Get the last digit
        # Example: 153 % 10 = 3
        digit = num % 10
        # Add digit raised to the power of number of digits
        # Example: 3³ + 5³ + 1³
        sum = sum + digit ** digits
        # Remove the last digit
        # Example: 153 // 10 = 15
        num = num // 10

    # Check whether calculated sum equals original number
    if sum == original:
        print(sum)

# Q3) Write a program to find the factorial of the given number

num = int(input("enter number to finde a factorial :"))

# Initialize factorial with 1
# We use 1 because multiplying by 1 does not change the value
fact = 1

# Loop from 1 to num
# Example: if num = 5, loop runs for 1, 2, 3, 4, 5
for i in range(1, num + 1):
    # Multiply fact with the current value of i
    # Example: 1 × 2 × 3 × 4 × 5 = 120
    fact = fact * i

print("the factorial of",num,"is :", fact)

# Q4 Write a program to print the factorial of all the given numbers between the two given
# numbers

num = int(input("enter 1st number :"))
num1 = int(input("enter last number :"))

for i in range(num + 1, num1):
    fact = 1

    for j in range(1, i + 1):
        fact = fact * j

    print(i ,"=",fact)

#Q5) Write a program to check whether the given number is prime or not

num = int(input("enter a number to check prime or not :"))

if num <= 1:
    print("the number is not prime")
else:
    flag = True

    for i in range(2, num + 1 ):
        if num % 2 == 0 :
            flag = False
            break

    if flag == True:
        print("the number is prime ")
    else:
        print("the number is not prime")

# Q6Write a program to print all the prime numbers between 1 and 100.

for num in range(2, 101):
    flag = True

    for i in range(2, num):
        if num % i == 0:
            flag = False
            break
    if flag == True:
        print(num)

# 7) Write a program to print the following pattern
# 1
# 2 1
# 1 2 1
# 2 1 2 1
# 1 2 1 2 1
for i in range(1, 6):
    for j in range(i):
        if((i - j)% 2 == 0):
            print(2,end=" ")
        else:
            print(1,end=" ")
    print()
#  second trick for do this pattern:
x = 1
for i in range(1, 6):
    for j in range(i):
        print(x,end=" ")

        if x == 1:
            x = 2
        else:
            x = 1
    print()
