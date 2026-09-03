# Programs for strings
# 1	Print multiple lines using single print statement. as – 
#                      I like “Python Programming” very much
#                      It is my favorite subject
print('''I like "Python Programming" very much
It is my favorite subject''')

# 2.	Print a part of the above string “very much” using the slice operator. 
s = 'I like "Python Programming" very much'

print(s[28:])

# 3.	Print the last 5 characters from the above given string

s = 'I like "Python Programming" very much'

print(s[-5:])

# 4.	Print all the characters in small letters. Also print all the even number position character.

s = 'I like "Python Programming" very much'

print("Lowercase:")
print(s.lower())

print("Even position characters:")
print(s[1::2])

# 5.	Take two strings as input from the user and concatenate them.

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

result = s1 + s2

print("Concatenated string:", result)

# 6.	Take a number and a string from the user and repeat the string for that many times.

s = input("Enter a string: ")
n = int(input("Enter a number: "))

print(s * n)

# 7.	Create a menu driven program for string manipulation
# a.	Find the length of a string
# b.	Print the string in upper case
# c.	Print the string in lower case
# d.	Print the string with initial capital
# e.	Split the string based on the character entered.


s = input("Enter a string: ")

print("\n1. Find length")
print("2. Convert to uppercase")
print("3. Convert to lowercase")
print("4. Initial capital")
print("5. Split the string")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Length:", len(s))

elif choice == 2:
    print("Uppercase:", s.upper())

elif choice == 3:
    print("Lowercase:", s.lower())

elif choice == 4:
    print("Initial capital:", s.title())

elif choice == 5:
    ch = input("Enter character for splitting: ")
    print(s.split(ch))

else:
    print("Invalid choice")

# 8  Input a string and check whether the given string is plaindrome or not

s = input("Enter a string: ")

reverse = s[::-1]

if s == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")

# 9 Input a string and print it in the reverse order using range

s = input("Enter a string: ")

for i in range(len(s) - 1, -1, -1):
    print(s[i], end="")

# 10 Take a string as an input from the user. Find total number of vowels in it. 

s = input("Enter a string: ")

count = 0

for ch in s:
    if ch in "aeiouAEIOU":
        count = count + 1

print("Total vowels:", count)

# 11Take two strings as input s1 and s2 and check whether s2 is present in s1 or not.
s1 = input("Enter first string:")
s2 = input("enter second string:")
if s2 in s1:
    print("s2 is present in s1")
else:
    print("s2 is not present in s1")
# 12.If s2 is a part of s1 then print the 1st and last occurrences of it.
s1 = input("enter 1st string:")
s2 = input("enter 2nd string:")
if s2 in s1:
    first = s1.find(s2)
    last = s1.rfind(s2)

    print("first occurrence:",first)
    print("last occurrence:",last)
else:
    print("s2 is not present in s1")
# 13.If s2 is present in s1 then also count number of times it occurs in s1.
s1 = input("enter 1st string:")
s2 = input("enter 2nd string:")
if s2 in s1:
    count = s1.count(s2)
    print("s2 occurs",count,"times")
else:
    print("s2 is not present in s1")
# 14.Count total number of words in the string input by user
string = input("enter string:")
words = string.split()
count = len(words)
print("total number of words:",count)
# 15.Take an input character from the user and check whether that character is present in the above given string or not. – Using ‘in’ operator and using ‘not in’ operator
s = input("enter a string:")
ch = input("enter a character:")
# using in.
if ch in s:
    print("character is present")
else:
    print("character is not present")
#using not in.
if ch not in string:
    print("character is not present")
else:
    print("character is present")
