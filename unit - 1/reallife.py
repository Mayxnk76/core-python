# this is the normal print to show the user that which movie thay want to watch
print("*------------*------------*")
print("Here is your favorite movies")
print("1. KGF ticket : 700")
print("2. KGF2 ticket : 700")
print("3. RRR ticker :700")
print("4. Toxic ticket :700")
print("5. Bahubali 2 ticket :700")
print("*------------*------------*")

c_ticket = 300
a_ticket = 700
s_ticket = 500
name = input("Enter your name :")
ch = int(input("Enter your movie choice number: "))
day = input("you are coming in weekend (YES or NO):")
person = input("Watch with family (YES OR NO): ")

if day == "YES":
    add1 = c_ticket + 100
    add2 = a_ticket + 100
    add3 = s_ticket + 100
if day == "YES":
        if child =="YES" and adult == "YES" and senior == "YES":
                 temp1 = add1 * child
                 temp2 = add2 * adult
                 temp3 = add3 * senior
        print("thank you for coming your total is this :", temp1 + temp2 + temp3)
if person == "YES":
    child = int(input("Enter number of children coming to watch: "))
    adult = int(input("Enter number of adult's are coming to watch:"))
    senior = int(input("Enter number of senior's are coming to watch :"))

    if child == 1 and adult == 1 and senior == 1:
        normal1 = c_ticket
        normal2 = a_ticket
        normal3 = s_ticket
        print("thank you for coming your total is this :",normal1 + noraml2 + normal3)
    else:
        mul1 = c_ticket * child
        mul2 = a_ticket * adult
        mul3 = s_ticket * senior
        print("thank you for coming your total is this :", mul1 + mul2+ mul3)
#   elif child =="NO" and adult == "NO" and senior == "NO":
#       temp1 = c_ticket
#       temp2 = a_ticket
#       temp3 = s_ticket
else:
    print("Answer only YES or NO")

print("thank you for coming your total is this :",)

             



    