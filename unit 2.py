# UNIT - 2
# Program Control Flow and Strings basic programs

# 1. Find the minimum and maximum of 2 numbers
a = 10
b = 20

minimum = min(a,b)
maximum = max(a,b)
print(f"minimum :",minimum,"maximum :",maximum)
# second trick
if b > a:
    print("the maximum number is :",b)
    print("the minimum number is :",a)

# 2. Write a program to find the maximum of three numbers
a = 10
b = 20
c = 30
if a > b and a > c:
    print("the maximum number is :",a)
elif b > a and b > c:
    print("the maximum number is :",b)
else:
    print("the maximum number is :",c)

# 3. Write a program to input the salary (basic) and calculate the net salary after
# adding da , hra and deducting the pf amount based on the conditions given.
# If basic is &lt;10000 then da=25%, hra=5%. If basic&gt;=10000 and basic
# &lt;=30000 then dat=35%, hra=10%. If basic &gt;30000 then da=40%, hra=20%.
# Pf is same for all 12%.

b_sal = int(input("enter basic salary :"))

if b_sal < 10000:
    da = (b_sal*25)/100
    hra = (b_sal*5)/100
    pf = (b_sal*12)/100
    net_sal =b_sal + da + hra - pf
    print("The net salary according to your salary is :",net_sal)
elif b_sal >= 10000 and b_sal <= 30000:
    da = (b_sal*35)/100
    hra = (b_sal*10)/100
    pf = (b_sal*12)/100
    net_sal =b_sal + da + hra -pf
    print("the net salary according to your salary is :",net_sal)
elif b_sal > 30000:
    da = (b_sal*40)/100
    hra =(b_sal*20)/100
    pf = (b_sal*12)/100
    net_sal =b_sal + da + hra -pf
    print("the net salary according to your salary is :",net_sal)
else:
    print("plz enter valid salary")

# 4. Print 1 to 10 numbers in ascending and descending order using range

for i in range(1,11):
    print(i)
for i in range(10,0,-1):
    print(i)

# 5. Print odd numbers between 1 to 50
for i in range(1,51):
    if i % 2 == 1:
        print(i)

# 6. Print the ‘*’ patterns using range()

for i in range(1, 6):
    for j in range(i):
        print("*",end=" ")
    print()

for i in range(1,6):
    for j in range(6 - i):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()

for i in range(1,6):
    for j in range(i):
        print(" ",end=" ")
    for j in range(1, 6-i):
        print("*",end=" ")
    print()
