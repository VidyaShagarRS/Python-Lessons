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

# (formatted Strings)
first_name= "Vidya"
last_name= "Shagar"
normal_concatenating= '['+first_name+" "+last_name+'] is now learning a python'
formatted_string= f"[{first_name} {last_name}] is now learning a Python"
print(normal_concatenating)
print(formatted_string)

