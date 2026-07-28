
#Q1 Arithmethic Opretion
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

print("addition =",num1 + num2)
print("subtraction =",num1 - num2)
print("division =",num1 / num2)
print("multiplicatin =",num1 * num2)
print("moduls = ",num1 % num2)

#Q2 Float number division

n1 = float(input("enter first number: "))
n2 = float(input("enter second number: "))

print("integer division =",n1 // n2)

# Q3 Swap two numbers

a = int(input("enter first number: "))
b = int(input("enter second number: "))

a, b = b, a

print("After swaping")
print("a =", a)
print("b =", b)

# Q4 Find net salary

basic = int(input("Eneter basic salary:"))
hra = int(input("Eneter hra :"))
da =int(input("Eneter da :"))
pf =int(input("Eneter pf :"))

net = basic + hra + da - pf

print("Net salary is :", net)

# Q6 check even or odd

num = int(input("enter number: "))

if num % 2 == 0:
    print("even number")
else:
    print("odd number")
