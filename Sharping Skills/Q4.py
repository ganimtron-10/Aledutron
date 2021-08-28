#Setup Code
import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

###########################################
#Real Code Starts

#Question and Its Code
#Turbo Sort Problem Code: TSORT

# Method 1
arrofnum = []

for i in range(int(input())):
    n = int(input())
    arrofnum.append(n)

for i in sorted(arrofnum):
	print(i)

#Method 2
arrofnum = []

for i in range(int(input())):
    n = int(input())
    arrofnum.append(n)
 
arrofnum.sort()

for i in arrofnum:
    print(i)

#Method 3

t = int(input())

arr = [int(input()) for i in range(t)]

for i in sorted(arr):
	print(i)



#List Compression

#Syntax variablename = [{the iterator} {for loop}]

# l = [i.isupper() for i in "RangE(1,10,2)"]
# print(l)