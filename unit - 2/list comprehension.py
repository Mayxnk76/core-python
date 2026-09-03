# 1) Write a program to make a list of alphabets and put all the elements in the other
#   list except vowels

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z']
cons = [x for x in a if x not in "aeiou"]
print(cons)
# 2) Write a program to create a list of words. Create another list and copy only the
# palindrome words in the new list
words = ["madam", "hello", "level", "python", "radar", "world"]

palin = [x for x in words if x == x[::-1]]
print("palindrome words :",palin)

# 3) Write a program to create a list of 20 numbers. Put only those numbers divisible
# by 2 and 3 in the another list.

num = [1, 2, 3, 6, 8, 9, 12, 15, 18, 20,
           21, 24, 25, 27, 30, 32, 36, 40, 42, 45]

result = [x for x in num if x % 2 == 0 and x % 3 == 0]
print("number divisible by 2 and 3 :",result)

# 4) Write a program to create a list of 5 subject marks. put the marks greater than 60 in another list

mark = [45, 65, 76, 54, 89]

result = [x for x in mark if x > 60]
print("marks greater than 60:",result)

# 5) Write a program to check whether the given number is prime or not using list
#    comprehension.

num = int(input("eneter a number :"))
d = [x for x in range(1, num+1)if num % x == 0]
if len(d)==2:
    print("The number is prime")
else:
    print("The number is not prime")

 # 6) write a program to copy only the three digit numbers into another list
 # [10,101,2,100,405,6]
 #          [101,100,405]

num = [10,20,101,400,350]
r = [x for x in num if x >= 100 and x <= 999]
print("Three digit number :",r)

# second trick
t = [x for x in num if len(str(x))==3]
print("Three digit number :",t)