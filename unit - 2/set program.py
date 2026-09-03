# Program based on Sets
# Q-1 A college has two groups of students enrolled in Python and Java courses.

ps= {"Amit", "Rahul", "Priya", "Neha", "Karan", "Sneha"}
js= {"Rahul", "Neha", "Karan", "Vivek", "Pooja", "Amit"}

# Perform the following:
# 1.Find students enrolled in both courses.
s_in_both = ps & js
print("Student enrolled in both courses:",s_in_both)

# 2.Find students enrolled only in Python.
s_in_py = ps - js
print("Student enrolled only in python:",s_in_py)

# 3.Find students enrolled only in Java.
s_in_j = js - ps
print("Student enrolled only in js:",s_in_j)

# 4.Find the list of all unique students.
all = ps | js
print("all unique student :",all)

# 5.Find students who are enrolled in exactly one course.
one = ps ^ js
print("enrolled in exactly one course:",one)

# 6.Check whether all Python students are also Java students.
if js .issuperset(ps):
    print("all student are python and java student")
else:
    print("all student are not python and java student")

# Q-2 Remove Duplicate Student Roll Numbers
# The following roll numbers were recorded during attendance:

r_num = [
    101, 102, 105, 101, 103, 107, 105,
    108, 102, 110, 103, 111, 108
]
print(r_num)
roll = set(r_num)
# Write a program to:
# 1.Find all unique roll numbers.
uni = roll & roll
print("unique roll number :",uni)
# 2.Find the total number of unique students.
total_uni = len(uni)
print("the total number of unique roll number is :",total_uni)
# 3.Find how many duplicate entries exist.
total = len(r_num)
com = total- total_uni
print("Duplicate roll number :",com)
# Display the original list and the list after removing duplicates.
