# Q1) Create a list of students say L1.
from itertools import count

l = ["nayan","mina","nayan","manish","arjun"]
#
# # Q2) Count total number of students from the list.
#
# print(len(l))
#
# #Q3) Add one more student in the list L1.
#
# l.append("amit")
# print(l)
#
# #Q4) Display all the students in the sorted order.
#
# l.sort()
# print(l)

# # Q5)Check a particular student’s name is present in the list or
# # not.
#
# name = input("enter name :")
#
# if name in l:
#     print("the name is present in the list")
# else:
#     print("the name is not present in the list")

# # Q6) If the student’s name is present in the list, print total
# # number of same name students in the list L1 and display
# # the position of 1st student.
#
# name = input("enter name :")
#
# print(l.count(name))
# print(l.index(name))

# # Q7 Remove the last student from the list L1.
#
# l.remove("mina")
# print(l)

# # Q8Remove a particular student from the list. (Take a name of
# # student from the user).
#
# name = input("enter name :")
#
# l.remove(name)
# print(l)

# # Q9 While removing the student from the list, if multiple
# # students have same name then remove all of them from
# # the list.
#
# name = input("enter name :")
#
# for i in l:
#     if name == i:
#         l.remove(i)
#         print(l)

# # Q10 Create a list of 10 numbers and find the maximum
# # and minimum numbers from it.
#
# num = [10,50,35,55,78,89,90,111,67,222]
#
# print(max(num))
# print(min(num))

# # Q11 Create a list of alphabets and count total number of
# # vowels in it.
#
# a = ['a', 'b', 'e', 'f', 'i', 'j', 'o', 'p', 'u', 'x']
#
# vowels = ['a', 'e', 'i', 'o', 'u']
#
# count = 0
# for i in a:
#      if i in vowels:
#          count = count + 1
#
# print("number of vowels :",count)

# # Q12 Create a list of even numbers between 1 to 21 using
# # range ().
# even = []
# for i in range(1, 22):
#     if i % 2 == 0:
#         even.append(i)
# # # there is second method to do this :
# l1 = list(range(2, 22, 2))
# print(l1)
# print(even)

# # Q13 Create a list of even numbers between 1 to 21 using
# # range ().
#
# l1 = [10,15,25,30,56,88,12,6,9,12]
#
# even = 0
# odd = 0
#
# for i in l1:
#     if i % 2 == 0:
#         even = even + i
#     else:
#         odd = odd + i
# print("total evan number is :",even)
# print("total of odd number is:",odd)
