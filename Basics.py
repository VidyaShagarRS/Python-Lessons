# (Variable and String concatenating)

name= input("What is your Name? ")
color= input("what is your favourite color? ")
print(name+" like "+color)

# (Variable Type Conversion)

weight_in_pounds= input("What is your weight in pounds? ")
converting_value= "0.453592"
weight_in_kg= int(weight_in_pounds) * float(converting_value)
print("Your weight in KG is:")
print(weight_in_kg)

# (Long Message String)

message= '''Hello all,
Its just
  an
Example
 long
message'''
print(message)

# (Length in Variables)

course="Here is an example"
print(course[0:9])
print(course[11:-3])
print(len(course))

# (formatted Strings)
first_name= "Vidya"
last_name= "Shagar"
normal_concatenating= '['+first_name+" "+last_name+'] is now learning a python'
formatted_string= f"[{first_name} {last_name}] is now learning a Python"
print(normal_concatenating)
print(formatted_string)

# (String Methods)

Inbuild_methods= "Here we can learn the In-Build methods for string"
print(Inbuild_methods)
print(Inbuild_methods.upper())
print(Inbuild_methods.lower())
print(Inbuild_methods.title())
print(Inbuild_methods.find("In-Build"))
print(Inbuild_methods.replace("methods", "functions/methods"))
print("learn" in Inbuild_methods)
print("learnt" in Inbuild_methods)

# (Arithmetic Operators)

print("10 + 3 (addition)")
print("10 - 3 (subtraction)")
print("10 * 3 (multiplication)")
print("10 / 3 (division but it gives output in float like 3.333)")
print("10 // 3 (division but it gives output in Int like 3.0 {Rounded result} )")
print("10 % 3 (modulus, it gives the remainder of division)")
print("10 ** 3 (It means 10 power of 3, output is \"1000\")")

# (If Statement)

print('''if ... :
        print("if condition is True")
elif ... :
        print("else if condition is True")
else :
        print("else True")
''')

# (Logical Operator)

print('''
and operator { if true and true : It executes the condition}
or  operator { if true or false : It executes either one condition is true}
not operator { if true and not bool condition : It executes Both are true, but not operator inverse the boolean value}''')

# (Comparision Operator)

print('''
>  {greater than}
<  {Lesser than}
>= {Greater than or equal to}
<= {Lesser than or equal to}
== {Comparing is equal to}
!= {Comparing is not equal to} ''')

# (While Loop)

lst=[10, 99, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95]
#Type your code here.
add_num = lst[5]
if (add_num == 59):
    while add_num <100:
        add_num +=1

        print(10 in lst)
print("There is a "+str(add_num)+" at index no:5")

# (Another Exampe)

line = '*'
max_length = 10

while len(line) <= max_length:
    print(line)
    line += "*"

while len(line) > 0:
    print(line)
    line = line[:-1]

# (Another Exampe)

print("Ask Help If You Need!")
count= 0
counts_Attempted= 4

while count < counts_Attempted :
     needhelp= input(">>> ").lower()
     count+=1
     if needhelp == "help":
         print('''"START" - To Start the CAR
"STOP - To Stop the CAR
"QUIT" - EXit''')
     elif needhelp == "start":
         print("Car Started")
         break
     elif needhelp == "stop":
         print("Car Stopped")
         break
     elif needhelp == "quit":
         break
     elif needhelp != "start" or "stop" or "help" or "quit":
         print("Please type Help")
else:
     print("I Don't Know What You Said!!!")
