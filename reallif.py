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
if person == "YES":
    child = int(input("Enter number of children coming to watch: "))
    adult = int(input("Enter number of adult's are coming to watch:"))
    senior = int(input("Enter number of senior's are coming to watch :"))

    if day.lower()=="YES":
        add1 = c_ticket + 100
        add2 = a_ticket + 100
        add3 = s_ticket + 100

    child_total = c_ticket * child
    adult_total = a_ticket * adult
    senior_total = s_ticket * senior

    total = child_total + adult_total + senior_total

    print("Thank you for coming",name)
    print("Your total is :",total)
elif person == "NO":
    if day == "NO":
        choice = input("you are (adult = a or senior = s) ? :")
        if choice == "a":
            print("you Total is :",a_ticket)
        elif choice == "s":
            print("your total is :",s_ticket)
        else:
            print("enter valid detali plz")
    else:
        choice = input("you are (adult = a or senior = s) ? :")
        if choice == "a":
            print("you Total is :", a_ticket + 100)
        elif choice == "s":
            print("your total is :", s_ticket + 100)
        else:
            print("enter valid detali plz")
else:
    print("Answer only YES or NO")





