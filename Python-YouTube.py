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

# Errors and Error Handling


# try:
# 	sum = 1 + 5
# 	print(sum)
# except NameError:
# 	x = 1
# finally:
# 	sum = 1 + 1
# 	print(sum)


# def cal(a):
# 	if type(a) == int:
# 		print(a)
# 	else:
# 		raise TypeError("parameter is not an int.")

# cal(True)


# assert 2+2 == 4
# print("Yess")

# assert 3 == 4
# print("no")

#--------------------------------------------------------


# file = open("output.txt","w")
# file.write("Hii\n")
# file.writelines("This is Python Lover...")
# file.close()


# inp = open("input.txt","r")
# data = inp.read()
# out = open("output.txt","w")
# out.write(data)
# out.close()
# inp.close()

# x = input()
# print("Hii!! This is {}.".format(x))
# dic = {}

# def divis(d):
# 	for i in range(2,d):
# 		for j in range(1,i):
# 			if i%j == 0:
# 				if i in dic.keys():
# 					dic[i] += [j]
# 				else:
# 					dic[i] = []

# t = int(input())
# for i in range(t):
# 	d = int(input())
# 	divis(d)

# print(dic)

#index 0 1 2 3 4 5 6 7

# print(nl[0][4])


# n = int(input())
# a = []
# for i in range(n):
# 	a.append(int(input()))

# a.sort()
# print(a)
# print(len(a))

# x.reverse()

# new_list = x[::-1]



# print(x)
# print(new_list)

# x = [1,2,3,4,5,67,89,45,1,2,3,8]

# y = [100,101,34]

# nl = [[1,2,3,4,5],['a','b', 'c'],[]]

# print("b" in nl[1])

#------------------------------------------------------#
#------------------------------------------------------#
#------------------------------------------------------#
import sys

sys.stdin = open("input.txt","r")
sys.stdout = open("output.txt","w")
#------------------------------------------------------#
#------------------------------------------------------#
#------------------------------------------------------#


# Dictionary
# key: value
# eg. key1: "Home"
# 	key2: "car"
# 	key3: "bike"

# keyd = {
# 	'key1': "Home",
# 	'key2': "car",
# 	'key3': "bike"
# }

# keyd['key1'] = "Flat"

# keyd['key4'] = "VillageHouse"

# print('key5' in keyd)

# d = {
# 	78 : 45,
# 	67 : 'str',
# 	's': [1,3],
# 	0 : False,
# 	1: True
# }

# print(list(d.values()))

#--------------------------------------

# Tuples

# con = 'sam','rahul','sam','anne'

# print(con.index('sam'))

#-------------------------------------

# Sets

# d = {1,2,3,4,5,6,3,2,1}

# e = {1,3,5,7,9}

# print(d,e)
# print(e | d)
# print(e & d)
# print(e - d)
# print(d - e)
# print(e ^ d)

#------------------------------------

# s = "123"

# # int(s)
# # bool()
# # str()
# # float()

# print(s,type(s))

# s = int(s)

# print(s,type(s))

# s = float(s)

# print(s,type(s))

# s = str(s)

# print(s,type(s))

# s = bool(s)

# print(s,type(s))
# def even(n):
# 	if n%2 == 0:
# 		return True
# 	else:
# 		return False

# f = input().split(" ")

# s = input().split(',')

# f = list(map(int,f))

# f = list(filter(even,f))

# print(f)
# print(s)

#----------------------------

# poly = lambda x: x**3 + 2*x + 5

# print(poly(10))


# Generators

# def countdown(n):
# 	for i in range(n,0,-1):
# 		yield i


# for i in countdown(5):
# 	print(i)

#-------------------------------------------

# Binary and Bitwise Operators

# Decimal
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10


# Binary
# 0
# 1


# Conversion Of Decimal To Binary:

# 59 - Decimal

# 2 | 59	1
# 2 | 29	1
# 2 | 14	0
# 2 | 7	1
# 2 | 3	1
#   | 1


# 111011 -> Binary (59)

# 49 - Deciaml


# 2 |  49		1
# 2 |  24		0
# 2 |  12		0
# 2 |  6		0
# 2 |  3		1
#   |  1


# 110001 -> Binary (49)

#--------------------------------------

# t = int(input())

# for i in range(t):
# 	n = int(input())
# 	l = list(map(int,input().split(' ')))
# 	total = 0
# 	l.sort()
# 	l.reverse()
# 	total = (l[0]*l[1]) + max(l[0]-l[1],l[1]-l[0])
# 	print(total)

#---------------------------------------------

# Number System and Binary and Bitwise operator (python)


# Decimal -> 10 -> (0-9)

# Binary -> 2 -> (0-1)

# Hexadecimal -> 16 -> (0-9 a-f)

# Octal -> 8 -> (0-8)



# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10


# 0
# 1

# 10
# 11

# 100
# 101


# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# a
# b
# c
# d
# e
# f
# 10




# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8

# Binary

# 0 and 1

# Binary -> Decimal

# 2 -> 10

# Decimal -> Binary

# 48 -> 110000

# 2 | 48  0
# 2 | 24  0
# 2 | 12  0
# 2 | 6   0
# 2 | 3   1
#   | 1


# 109 -> 1101101


# 2 | 109  1
# 2 | 54  0
# 2 | 27  1
# 2 | 13  1
# 2 | 6  0
# 2 | 3  1
#  | 1  



# def decitobin(n):
# 	binaryrep = ''
# 	while n>=1:
# 		binaryrep = str(n%2) + binaryrep
# 		n = n//2
# 	return(binaryrep)

# print(decitobin(4))
# print(bin(4)[2:])
# print(oct(48))



# 563 == 5*10^2 + 6*10^1 + 3*10^0

# 100 == 1*2^2 + 0*2^1 + 0*2^0
# 		4		0		0 = 4


# def bintodeci(n):
# 	n = str(n)
# 	deciformat = 0
# 	for i in range(len(n)):
# 		k = len(n) - 1 - i
# 		deciformat += int(n[i])*(2**k)

# 	return deciformat

# print(bintodeci(110000))

# print(int('1101101',2))



# print(oct(100))

# print(int('144',8))

#---------------------------------------

# Number System and Binary and Bitwise operator (python)


# Decimal -> 10 -> (0-9)

# Binary -> 2 -> (0-1)

# Hexadecimal -> 16 -> (0-9 a-f)

# Octal -> 8 -> (0-8)



# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10


# 0
# 1

# 10
# 11

# 100
# 101


# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# a
# b
# c
# d
# e
# f
# 10




# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8

# Binary

# 0 and 1

# Binary -> Decimal

# 2 -> 10

# Decimal -> Binary

# 48 -> 110000

# 2 | 48  0
# 2 | 24  0
# 2 | 12  0
# 2 | 6   0
# 2 | 3   1
#   | 1


# 109 -> 1101101


# 2 | 109  1
# 2 | 54  0
# 2 | 27  1
# 2 | 13  1
# 2 | 6  0
# 2 | 3  1
#  | 1  



# def decitobin(n):
# 	binaryrep = ''
# 	while n>=1:
# 		binaryrep = str(n%2) + binaryrep
# 		n = n//2
# 	return(binaryrep)

# print(decitobin(4))
# print(bin(4)[2:])
# print(oct(48))



# 563 == 5*10^2 + 6*10^1 + 3*10^0

# 100 == 1*2^2 + 0*2^1 + 0*2^0
# 		4		0		0 = 4


# def bintodeci(n):
# 	n = str(n)
# 	deciformat = 0
# 	for i in range(len(n)):
# 		k = len(n) - 1 - i
# 		deciformat += int(n[i])*(2**k)

# 	return deciformat

# print(bintodeci(110000))

# print(int('1101101',2))



# # print(oct(100))

# # print(int('144',8))

# # bitwise operator

# and  -> &
# or  -> |
# not -> ~
# xor  -> ^
# left shift  -> <<
# right shift -> >>



# # truth tables

# and 
# 1 1  1
# 1 0  0
# 0 1  0
# 0 0  0

# or
# 1 1  1
# 1 0  1
# 0 1  1
# 0 0  0

# not (1's complement)

# ~1 == -(1+1) 
# 	  -(10)2
# 	  -(2)10


# xor -> addtion (binary)
# 1 1 0
# 1 0 1
# 0 1 1
# 0 0 0


# n << x == n*2^x

# 0000 1010 << 3 ==  0101 0000



# n >> x == n/2^x


# 0000 1101 >> 2 == 0000 0011





# print(~5)# 101 = -(101+1) = -(110) = -6

# print(1000 << 3)# 0001 == 0100 = 4
# print(200 >> 10)



# print(45|89)

# print(bin(45),bin(89))


# #   0101101
# # | 1011001
# #   1111101

# print(int('1111101',2))

#------------------------------------------------------#

# Object Oriented Programming OOP

#class Mobile:
#	osid = 100
#	charging = False
#	def __init__(self,name,battery,memory):
#		self.name = name
#		self.battery = battery
#		self.memory = memory
#
#	def __sub__(self,other):
#		return (self.battery - other.battery, self.memory - other.memory)
#
#	@classmethod
#	def Iphone(cls,battery,memory):
#		return cls("Iphone Mobiles",battery,memory)
#	
#	@staticmethod
#	def checkvirus(apps):
#		if apps == "virus":
#			raise TypeError
#		else:
#			return True
#
#	@property
#	def ischarging(self):
#		return self.charging
#
#	@ischarging.setter
#	def ischarging(self,value):
#		self.charging = value
#
#
#
#m1 = Mobile("M1",8000,64)
#m2 = Mobile("M2",6000,128)
#
#print(m2.ischarging)
#
#m2.ischarging = 99
#
#print(m2.ischarging)


# print(m1-m2)
# print(m2.__sub__(m1))
# print(Mobile.osid)

# i1 = Mobile.Iphone(5000,128)
# print(i1.name,i1.battery,i1.memory)

# apps = ["youtube","instagram","virus","temple run","clock"]
# for app in apps:
# 	Mobile.checkvirus(app)


# __add__
# __sub__
# __mul__
# __truediv__
# __floordiv__
# __mod__
# __pow__
# __and__
# __or__
# __xor__






