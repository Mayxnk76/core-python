# Q1 print the even number between 1 to 100 using loop

for i in range(2 , 101, 2):
    print(i)

# Q2 print the value is prime or not

num = int(input("enter number: "))

if num <= 1:
    print("The number is not prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("The number is not prime")
            break
    else:
        print("The number is prime")
