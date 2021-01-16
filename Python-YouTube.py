# Data Types

# Numbers
# 		int -> whole numbers
# 		eg. 100, 50000,123, 567 etc

# 		float -> decimal
# 		eg. 1.2 65.456 3.142 2.71 etc


# Text
# 		string -> series of text
# 		eg "HI! I am A Coder..."
# 		eg. "123" "3.142"
# 		char -> single letter
# 		eg. 'a', 'A'

# Boolean/Bool
# 		true 1
# 		false 0

# Variables

# Task:

# Hii!! This is Pratik.
# Pratik is my friend.
# pratik also loves python.

# name1 ="Pratik"

# print("Hii!! This Is "+name1)

# Maths Operator

# operators (op)
# + add
# - sub
# * mul
# / div

# % modulus #remainder
# // quotient 
# ** exponent # power 


# a,b any numbers

# a op b
# a + b
# a - b
# a**b


# Tasks

# #----------------------------------------------
# Task 1:

# Hii!
# This is YOURNAME.
# I love "Python".
# My Age is "YOURAGE(6+x)"  Note:where x = YOURAGE-6
# #----------------------------------------------------
# Task 2:

# 1 on the die then we have to print "Hii"
# 6 on the die then we have to print "Out of the House."
# #-----------------------------------------------------


# print("Hello Bros!") 
# print("Hellos")
# print("H")
# print("1234" + "1")
# print("23456@$%^&*")
# print(1234 + 1)
# print(123/123)
# print(True)
# print(False)
# print(1342.0)

#--------------------------------------------------------

# Task:

# Hii!! This is Pratik.
# Pratik is my friend.
# pratik also loves python.


# name1 ="Ram"
# name2 = "sam"

# print("Hii!! This Is "+name2)
# print(name2 + " is my friend.")
# print(name2 + " also loves python.")
#---------------------------------------------------------
# a = 10
# b = 3

# print(a+b)

# print(a-b)

# print(a*b)

# print(a/b)

# print(a%b)

# print(a//b)

# print(a**b)


# sum = a+b


# print(sum)

#--------------------------------------------------------

# print("Coder said,'Hii!'")
# print('Coder said,"Hii!"')
# print("Coder said,\"Hii!\"")

# print("\\")
# print("\'")
# print("\t H")
# print("1. a\n2. b\n3. c")

# s1 = "Hii! This is "
# n1 = " Coder."

# print(s1+n1)

# print("1234567890"*11)

# print("""Hii! This is "coder".
# 	This is \ 'Python'.""")


#---------------------------------------------------------

# Boolean Comparions/Operator

# == /equality
# >  /greater than 
# <  /less than 
# >= /grater than equal to
# <= /less than equal to
# != /not equal to

# x = 10

# print(10 == x) # = -> assign and == -> checks equality

# print("Annie" > "Andy") # A>A n>n n>d -> 14>4

# print("A" == "a")

# In-Place Operators

# var = var + con -> var += con
# var %= con op={+,-,*,/,//,%,**,etc.}

# var = 10
# con = 20

# var **= con 

# print(var)


# Task:

# 1 on the die then we have to print "Hii"
# 6 on the die then we have to print "Out of the House."

#----------------------------------------------------------

# if cond:
# 	stmt

# dienum = 6

# if dienum == 1:
# 	print("HII")

# if dienum == 6:
# 	print("Out of the House.")


#----------------

# num = 9

# if num > 10:
# 	print("Greater than 10.")
# 	if num < 20:
# 		print("Number is between 10 and 20.")

#----------------

# if we get number 10 then only we have to print (Its Full)
# Otherwise we have to print(Its Half)

# number = 1

# if number == 10:
# 	print("Its Full")
# else:
# 	print("Its Half")

#--------------------------



# if day == 1:
# 	print("Monday")
# else:
# 	if day == 2:
# 		print("Tuesday")
# 	else:
# 		if day == 3:
# 			print("Wednesday")

# day = 1

# if day == 1:
# 	print("Monday")
# elif day == 2:
# 	print("Tuesday")
# elif day == 3:
# 	print("Wednesday")
# elif day == 4:
# 	print("Thursday")
# elif day == 5:
# 	print("Friday")
# elif day == 6:
# 	print("Saturday")
# else:
# 	print("Sunday")




# if cond:
# 	stmt
# elif cond2:
# 	stmt2
# elif con3:
# 	stmt4
# else:
# 	stmt3



# Boolean Logic
# and, not, or


# operators used in python
# a booleanlogic c

# and gives true only if a,b both are True
# or any one operation as true 
# not it will return opposite of the given boolean value


# a = 5
# b = 15
# c = 4

# if not a>b and a>c:
# 	print("one should be maximum")


#----------------------------------------------------------------------

# Loops

# 1. for
# 2. while


# for i in range(1,11):
# 	print("{main} X {multiple} = {ans}".format(ans=2*i,main=2,multiple=i))

# i = 1

# while i<10:
# 	print("{main} X {multiple} = {ans}".format(ans=2*i,main=2,multiple=i))
# 	i += 1 # i = i + 1

#----------------------------------------------------------------------------------

# function format:
# def fname(): -> definition
# 	stmts
# fname() -> calling

# def printing():
# 	print("Hello World!")

# printing()

# a = 5
# b = 10

# def calculate(b,a):
# 	print(b+a)
# 	print(b-a)
# 	print(b*a)
# 	print(b/a)

# calculate(a,b)
# calculate(100,50)
# calculate(a=10,b=50)

# argument -> defining
# parameter -> calling

# def intro(name,age,plang):
# 	introduction = """Hii!!
# This is {}.
# I am {} years Old.
# I love {}"""
# 	print(introduction.format(name,age,plang))

# intro("Coder",20,"Python")
# intro("Ninja",30,"Java")
# intro("Block",17,"C++")

# eg. function


# def expo(a,b):
# 	c = a**b
# 	return c

# ans = expo(2,3)
# print(ans)

# def calculate(b,a,func):
# 	print(b+a)
# 	print(b-a)
# 	print(b*a)
# 	print(b/a)
# 	print(func(b,a))


# calculate(1,50,expo)


# import random

# print(random.random())

#----------------------------------


