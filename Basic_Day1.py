
########## Print Statement in Python and Dealing with Quotes and Multi-line Strings ##########

print(1)
print("Hello Sabana", 1, "Sultana")
print("Hello Sabana", 1, "Sultana", sep="  /  ") #sep is used to change the default space between the values (delimerter= sep, end)
print("Hello Sabana", sep="/") 
print("Hello Sabana", end="***") #end is used to change the default new line at the end of the print statement
print("Hello Sultana")

print(''' HIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
      IIIIIIIIIIIIIIIIII ''')

print (""" HIIIIIIII
       
       IIIIIIIII """)

# print('hhhhh  -- error
# hhhhhhhh')

# print("hhhhh  -- error
# hhhhhhhh")

print(" Sabana 'Sultana' ")
print(' Sabana "Sultana" ')
# print(' Sabana 'Sultana' ') -- error
# print(" Sabana "Sultana" ") -- error

print(""" Sabana""")
# print(''' Sultana'''sultana'''  ) --error

print(" Sabana \"Sultana\" is a good girl ")   




########## Variables in Python ##########

print(10+20)

print ("sabna" + "sultana")

# print(10 + "20")  # error

print(10, "20")  # valid
print(10,20, sep=" + ")  # valid
print(10,20)

print("sabana",20)

# print("sabana"+20)  # error

print("sabana"+ str(20))  # valid

print ("20"+ str(20))  # valid
print (int("20")+ 20)  # valid
print (int("20")+ int("30"))  # valid

a = 10
b = 20
print(a + b)
name = "Sabana Sultana"
print("Hello " + name)
print("Hello ", name)
a=str(a)
print("Value of a is " + a)
print("Sabana "+ a)


########## Multiple Variable Assignment in Python ##########

x=y=z=100
print(x)
print(y)    
print(z)

x,y,z=10,20,30
print(x)    
print(y)
print(z)

''' This is a multi-line comment
    in Python
    we can use triple quotes to write multi-line comments
'''

total, average, grade = 290, 96.67, 'A'
print("Total:", total)
print("Average:", average)
print("Grade:", grade)
print(type(total))
print(type(average))
print(type(grade))

total_sum= 10+20+30+40+50
# total_sum_2=10+20+30
#             +40+50 # invalid syntax
print(total_sum)
# print(total_sum_2)
total_sum_3= (10+20+30
              +40+50) # valid syntax
print(total_sum_3)
total_sum_4= 10+20+30+ \
              40+50 # valid syntax   ## / will help to continue the statement in the next line
print(total_sum_4)

########## Python Identifiers ##########
# Valid Identifiers
myVariable = 10
_my_variable = 20
myVariable123 = 30
MYVARIABLE = 40
my_variable_name = 50
_myVariableName = 60
_myVariable_name_123 = 70
print(myVariable)
print(_my_variable)
print(myVariable123)
print(MYVARIABLE)
print(my_variable_name)
print(_myVariableName)
print(_myVariable_name_123)
# Invalid Identifiers
# 1myVariable = 10  # starts with a digit   
# my-Variable = 20  # contains hyphen
# my Variable = 30  # contains space
# my$Variable = 40  # contains special character $
# my@Variable = 50  # contains special character @
# my#Variable = 60  # contains special character #
# my%Variable = 70  # contains special character %
# my^Variable = 80  # contains special character ^

######## Type Conversion in Python ##########
num_int = 10
num_float = 15.5
num_str = "20"
print("Integer:", num_int, "Type:", type(num_int))
print("Float:", num_float, "Type:", type(num_float))
print("String:", num_str, "Type:", type(num_str))
# Converting Integer to Float
int_to_float = float(num_int)
print("Converted Integer to Float:", int_to_float, "Type:", type(int_to_float))
# Converting Float to Integer
float_to_int = int(num_float)
print("Converted Float to Integer:", float_to_int, "Type:", type(float_to_int))
# Converting String to Integer
str_to_int = int(num_str)
print("Converted String to Integer:", str_to_int, "Type:", type(str_to_int))
# Converting String to Float
str_to_float = float(num_str)
print("Converted String to Float:", str_to_float, "Type:", type(str_to_float))

s="10.56"
si=float(s)
print(si)
print(type(si))

# s="ten"
# si=int(s)  # ValueError: invalid literal for int() with base 10: 'ten'
# print(si)