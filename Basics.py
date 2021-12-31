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
print("10 // 3 (division but it gives output in Int like 3 {Rounded result} )")
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