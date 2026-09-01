# 1) create list of your mca subjects
from builtins import sum

subject = ["python","FSD","DBMS","SM","AI"]
print(subject)

# 2) create list of 6 friends
name = ["raju","ramu","nayan","mina","tina","mahek"]
print(name)

# 3) Display the using for loop (list of 10 numbers)

number = [10,20,30,40,50,60,70,80,90,100]
for i in number:
    print(i)

# 4) Display the list using range( list of 5 fruits and its price)

fruit = ["apple","banana","mango","orange","grapes"]
price = [100,50,80,60,120]
for i in range(len(fruit)):
    print(fruit[i],"=",price[i])

# 5) Display the list of 5 universities using while loop

uni = [ "Gujarat University",
    "Delhi University",
    "Mumbai University",
    "Pune University",
    "Rajasthan University"]
i = 0
while i < len(uni):
    print(uni[i])
    i = i + 1

# 6) Create a list of 10 numbers and find the sum of all the elements of the list

num = [10,20,30,40,50,60,70,80,90,100]
sum = 0
for i in num:
    sum = sum + i
print("sum of all elements :",sum)