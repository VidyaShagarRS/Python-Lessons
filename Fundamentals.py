# (If Else - Control Statements)

mark = 65

if (mark >= 90):
    print("Excellent")
elif (mark >=75):
    print("Good")
elif (mark >=50):
    print("Average")
else:
    print("Oops, You're Fail")

# Another Example

Age= int(input("Please Enter Your Age: "))
if Age > 5:
    Nationality= input("Please Enter Your Nationality: ")
    if Nationality.upper() == "INDIAN":
        print("You're Eligible")
    else:
        print("Your Nationality not met with Criteria")
else:
    print("Your Age not met with Criteria")

# Another Example

mark_1=int(input("mark 1: "))
mark_2=int(input("mark 2: "))
mark_3=int(input("mark 3: "))
if (mark_1 == mark_2 == mark_3):
    print("Equal")
else:
    print("Not Equal")
