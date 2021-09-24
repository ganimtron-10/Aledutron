#Setup Code
import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

###########################################
#Real Code Starts

# t = int(input())
# for i in range(t):
# 	a,b,c,d,e = map(int,input().split())
# 	if (a+b <= d and c <= e) or (a+c <= d and b <= e) or (b+c <= d and a <= e):
# 		print("Yes")
# 	else:
# 		print("No")

# for i in range(int(input())):
# 	n,a,b = map(int,input().split())
# 	s = input()
# 	print(s.count('0')*a + s.count('1')*b)


# for i in range(int(input())):
# 	n = int(input())
# 	a = list(map(int,input().split()))

# 	index_odd = index_even = 0
# 	array_odd = array_even = 0

# 	if n%2 == 0:
# 		index_odd = index_even = int(n/2)
# 	else:
# 		index_odd = int((n+1)/2)
# 		index_even = index_odd - 1

# 	for i in a:
# 		if i%2 == 0:
# 			array_even += 1
# 		else:
# 			array_odd += 1

# 	print(min(array_even,index_odd)+min(index_even,array_odd))

# for i in range(int(input())):
# 	n = input()
# 	x = list(map(int,input().split()))
# 	y = list(map(int,input().split()))

##############################################
# # Function for finding intersection between two sets (A&B)
# def intersection(lst1,lst2):
#     lst3=[]
#     for val in lst1:
#         if val in lst2:
#             lst3.append(val)
#     return lst3

# # Function for finding union of two sets (A|B)

# def union(lst1,lst2):
#     lst3=lst1.copy()
#     for val in lst2:
#         if val not in lst3:
#             lst3.append(val)
#     return lst3

# # Function for finding difference between two sets (A-B)

# def diff(lst1,lst2):
#     lst3=[]
#     for val in lst1:
#         if val not in lst2:
#             lst3.append(val)
#     return lst3

# # Function for finding symmetric difference of two sets (A^B)

# def sym_diff(lst1,lst2):
#     lst3=[]
#     D1=diff(lst1,lst2)
#     print("Difference between Cricket and Badminton (C-B) is : ", D1)
#     D2=diff(lst2,lst1)
#     print("Difference between Badminton and Cricket (B-C) is : ", D2)
#     lst3=union(D1,D2)
#     return lst3

# # Functon for finding List of students who play both cricket and badminton

# def CB(lst1,lst2):
#     lst3=intersection(lst1,lst2)
#     print("\n\nList of students who play both cricket and badminton is : ", lst3)
#     return len(lst3)

# # Function for finding List of students who play either cricket or badminton but not both

# def eCeB(lst1,lst2):
#     lst3=sym_diff(lst1,lst2)
#     print("\nList of students who play either cricket or badminton but not both is : ",lst3)
#     return len(lst3)


# # Function for finding Number of students who play neither cricket nor badminton

# def nCnB(lst1,lst2,lst3):
#     lst4=diff(lst1,union(lst2,lst3))
#     print("\n\nList of students who play neither cricket nor badminton is : ",lst4)
#     return len(lst4)

# #<--------------------------------------------------------------------------------------------------->

# # Function for finding Number of students who play cricket and football but not badminton

# def CFnB(lst1,lst2,lst3):
#     lst4=diff(intersection(lst1,lst2),lst3)
#     print("\n\nList of students who play cricket and football but not badminton is : ",lst4)
#     return len(lst4)

# #<----------------------------------------------------------------------------------------------------->

# # Main function

# # Creating list for SE COMP
# SEComp = ["AA","BB","CC","DD","EE","FF","GG","HH","II"]

# print("Original list of students in SEComp : " + str(SEComp))

# # Creating list for Cricket
# Cricket = ["AA","BB","CC","DD","EE"]

# print("The list of students playing cricket: " +str(Cricket))

# # Creating list for Football
# Football = ["DD","EE","FF","GG","HH","II"]

# print("The list of stXudents playing football :" +str(Football))

# # Creating list for Badminton
# Badminton = ["BB","CC","DD"]
# print("The list of students playing badminton :" +str(Badminton))

# print("\n Number of students who play both cricket and badminton : ", CB(Cricket,Badminton))
# print("\n Number of students who play either cricket or badminton but not both : ", eCeB(Cricket, Badminton))
# print("\n Number of students who play neither cricket nor badminton : ", nCnB(SEComp,Cricket,Badminton))
# print("\n  Number of students who play cricket and football but not badminton : ", CFnB(Cricket,Football,Badminton))

# ########################################
# # Function for average score of the class
# def average(marks):
#     sum=0
#     count=0
#     for i in range(len(marks)):
#         if marks[i]!=-1:
#             sum+=marks[i]
#             count+=1
#     avg=sum/count
#     print("Total Marks : ", sum)
#     print("Average Marks :", avg)

# #<----------------------------------------------------------------------------------------------------->

# # Function for Highest score in the test for the class

# def Maximum(marks):
#     Max=marks[0]
#     for i in range(len(marks)):
#         if marks[i]>Max:
#             Max=marks[i]
#     return(Max)

# #<------------------------------------------------------------------------------------------------------>

# # Function for Lowest score in the test for the class

# def Minimum(marks):
#     Min=marks[0]
#     for i in range(len(marks)):
#         if marks[i]<Min and marks[i]!=-1:
#             Min=marks[i]
#     return(Min)

# #<------------------------------------------------------------------------------------------------------->

# # Function for counting the number of students absent for the test

# def absentcount(marks):
#     count=0
#     for i in range(len(marks)):
#         if marks[i]==-1:
#             count+=1
#     return(count)

# #<------------------------------------------------------------------------------------------------------->

# # Function for displaying marks with highest frequency
# def maxFrequency(marks):
#     i=0
#     Max=0
#     print("Marks  |  Frequency")
#     for j in marks:
#         if (marks.index(j)==i):
#             print(j,"    |  ",marks.count(j))
#             if marks.count(j)>Max:
#                 Max=marks.count(j)
#                 mark=j
#         i=i+1
#     return(mark,Max)


# #<------------------------------------------------------------------------------------------------------->

# # Main function

# marksinFDS=[]
# numberofstudents=int(input("Enter total number of students : "))
# for i in range(numberofstudents):
#     marks=int(input("Enter marks of student"+str(i+1)+"(enter -1 in case of absent)"))
#     marksinFDS.append(marks)

# print("Average Marks")
# average(marksinFDS)
# print("Highest Score in Class : ", Maximum(marksinFDS))
# print("Lowest Score in Class : ", Minimum(marksinFDS))
# print("Number of Students absent in the test : ", absentcount(marksinFDS))
# mark,fr = maxFrequency(marksinFDS)
# print("Highest frequency is of marks {0} that is {1} ".format(mark,fr))
