# Q1 pattern
# *
# * *
# * * *
# * * * *
# * * * * *


for i in range(6):
    for j in range(i):
        print("*", end=" ")
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

for i in range(6):
    for j in range(i, 6):
        print("*", end=" ")
    print()

# Q4 pattern


for i in range(1, 5):
    for j in range(1, 5):
        print("*", end=" ")
    print()

# Q5 pattern
  #           *
  #         * *
  #       * * *
  #     * * * *
  #   * * * * *
  # * * * * * *
for i in range(6):
    for j in range(i, 6):
        print(" ", end=" ")
    for k in range(i + 1):
         print("*", end=" ")
    print()

# Q7 pattern
# * * * * * *
#   * * * * *
#     * * * *
#       * * *
#         * *
#           *
for i in range(6):
    for j in range(i + i):
        print(" ", end="")
    for k in range(i,6):
        print("*", end=" ")
    print()

# Q8 pattern

 #      *
 #     ***
 #    *****
 #   *******
 #  *********
 # ***********

for i in range(6):
    for j in range(i , 6):
        print(" ",end="")
    for j in range(i):
        print("*", end="")
    for k in range(i + 1):
        print("*", end="")
    print()


# Q9 pattern
      # ***********
      #  *********
      #   *******
      #    *****
      #     ***
      #      *
for i in range(6):
    for j in range(i + 6):
        print(" ",end="")
    for k in range(i, 6 - 1):
        print("*",end="")
    for k in range(i, 6):
        print("*",end="")
    print()


# Q9 pattern

for i in range(5):
    for j in range(i , 5):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    for j in range(i + 1):
        print("*",end="")
    print()
for i in range(5):
    for k in range(i + 1):
        print(" ",end="")
    for k in range(i, 5 - 1):
        print("*",end="")
    for k in range(i , 5):
        print("*",end="")
    print()