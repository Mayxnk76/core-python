# Q1 pattern
# *
# * *
# * * *
# * * * *
# * * * * *


for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")
    print()

# Q2 pattern
# *
# **
# ***
# ****
# *****
# ******
# *****
# ****
# ***
# **
# *
for i in range(1,6):
    print("*" * i)
for j in range(6, 0, -1):
    print("*" * j)

# Q3 pattern
# *****
# ****
# ***
# **
# *

for i in range(5, 0, -1):
    print("*" * i)

# Q4 pattern


for i in range(1, 5):
    for j in range(1, 5):
        print("*", end=" ")
    print()
